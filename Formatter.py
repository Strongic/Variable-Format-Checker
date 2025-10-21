import RecognizeErrors


class ASTProcessor:
    def __init__(self, variables=None):
        # Run issue detection and merge it into variables
        self.variables = self._merge_issues(variables) if variables else []

    def _merge_issues(self, variables):
        issues = RecognizeErrors.recognizeErrors(variables)
        variable_map = {(v["name"], v["line"], v["scope"]): v for v in variables}

        for err in issues:
            key = (err["name"], err["line"], err["scope"])
            if key in variable_map:
                variable_map[key]["issue"] = err["issue"]

        # Ensure all variables have an 'issue' key (None if clean)
        for var in variable_map.values():
            var.setdefault("issue", "None")

        return list(variable_map.values())

    def generate_header(self, variables):
        if not variables:
            variables = [{"name": "No Variable", "scope": "N/A", "line": "N/A", "issue": "None"}]

        max_var_length = max(len(var["name"]) for var in variables)
        max_scope_length = max(len(var["scope"]) for var in variables + [{"scope": "Scope"}])
        max_line_length = max(len(str(var["line"])) for var in variables + [{"line": "Line"}])
        max_issue_length = max(len(var.get("issue", "None")) for var in variables + [{"issue": "Issue"}])

        column_widths = [
            max(max_var_length, len("Variable")),
            max_scope_length,
            max_line_length,
            max_issue_length
        ]

        total_width = sum(column_widths) + 9  # account for ' | ' spacing

        header = f"""
Variable Name Analysis:
{'-' * total_width}
{'Variable'.ljust(column_widths[0])} | {'Scope'.ljust(column_widths[1])} | {'Line'.ljust(column_widths[2])} | {'Issue'.ljust(column_widths[3])}
{'-' * total_width}
"""

        return header, column_widths, total_width

    def generate_table(self, variables, column_widths, total_width):
        if not variables:
            return f"{'No Variable'.ljust(column_widths[0])} | {'N/A'.ljust(column_widths[1])} | {'N/A'.ljust(column_widths[2])} | {'None'.ljust(column_widths[3])}\n"

        rows = ""
        for var in variables:
            rows += f"{var['name'].ljust(column_widths[0])} | {var['scope'].ljust(column_widths[1])} | {str(var['line']).ljust(column_widths[2])} | {var.get('issue', 'None').ljust(column_widths[3])}\n"

        return rows
