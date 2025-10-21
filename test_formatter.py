import unittest
from Formatter import ASTProcessor  # Adjust based on the actual path
from RecognizeErrors import recognizeErrors  # Adjust based on the actual path
from VariableExtractor import VariableExtractor  # Adjust based on the actual path

# Example Python code snippets to generate test ASTs
example_asts = [
    """
a = 10
b = 20
def my_function(x, y):
    z = x + y
    return z
""",
    """
GLOBAL_VAR = 42

def another_function():
    global GLOBAL_VAR
    LOCAL_VAR = 10
    return LOCAL_VAR + GLOBAL_VAR
""",
    """
class MyClass:
    def __init__(self):
        self.instance_var = 1

    def method(self, param):
        local_var = param * 2
        return local_var
""",
    """
Absurd_variable_name_length_to_see_if_the_table_header_adjusts = 1 
def method(self, param):
        Absurd_variable_name_to_check_column_alignment_somehow_that_was_not_enough_chars_to_test = param * 2
        return local_var
""",
    """
# intentionally blank
"""
]


# Function to verify formatting output
def test_formatter_output_format(output, expected_headers):
    # Check headers presence
    for header in expected_headers:
        assert header in output, f"Missing column header: '{header}'"

    # Check for correct formatting of rows
    lines = output.splitlines()
    for line in lines:
        if "|" in line:
            parts = line.split('|')
            assert len(parts) == 4, f"Incorrect number of columns in row: {line}"

    print("Table formatting test passed.")


class TestFormatter(unittest.TestCase):

    def test_column_alignment(self):
        output = """
Variable Name Analysis:
-------------------------------------------------------------
Variable | Scope  | Line | Issue                           
-------------------------------------------------------------
a        | global | 2    | None                            
b        | local  | 3    | Naming Violation: Use snake_case
"""

        expected_headers = ["Variable", "Scope", "Line", "Issue"]

        print("Test Column Alignment")
        test_formatter_output_format(output, expected_headers)

    def test_empty_table(self):
        output = """
Variable Name Analysis:
-------------------------------------------------------------
Variable | Scope  | Line | Issue                           
-------------------------------------------------------------
No Variable | N/A | N/A | None
"""

        expected_headers = ["Variable", "Scope", "Line", "Issue"]

        print("Test Empty Table Handling")
        test_formatter_output_format(output, expected_headers)

    def test_duplicate_variables(self):
        output = """
Variable Name Analysis:
-------------------------------------------------------------
Variable | Scope  | Line | Issue                           
-------------------------------------------------------------
a        | global | 2    | None
a        | local  | 4    | Naming Violation: Use snake_case
"""

        expected_headers = ["Variable", "Scope", "Line", "Issue"]

        print("Test Duplicate Variables Handling")
        test_formatter_output_format(output, expected_headers)

    def test_special_characters_in_variables(self):
        output = """
Variable Name Analysis:
-------------------------------------------------------------
Variable | Scope  | Line | Issue                           
-------------------------------------------------------------
variable_with_underscore  | global | 2    | None
variable-with-hyphen      | local  | 3    | None
"""

        expected_headers = ["Variable", "Scope", "Line", "Issue"]

        print("Test Special Characters in Variables")
        test_formatter_output_format(output, expected_headers)

    def test_long_variable_names(self):
        output = """
Variable Name Analysis:
-------------------------------------------------------------
Variable | Scope  | Line | Issue                           
-------------------------------------------------------------
Absurd_variable_name_to_check_column_alignment_somehow_that_was_not_enough_chars_to_test | global | 2    | None
"""

        expected_headers = ["Variable", "Scope", "Line", "Issue"]

        print("Test Long Variable Names")
        test_formatter_output_format(output, expected_headers)

    def test_pass_fail_cases(self):
        for i, code in enumerate(example_asts, start=1):
            print(f"\nTest Case {i}:")
            print("=" * 50)

            # Extract variables
            extractor = VariableExtractor()
            variables = extractor.extract(code)

            # Display extracted variables (raw)
            print(f"Extracted Variables (Raw): {variables}")

            # Analyze for naming and scope issues
            errors = recognizeErrors(variables)

            # Merge error info into original variable list
            variable_map = {(v["name"], v["line"], v["scope"]): v for v in variables}
            for err in errors:
                key = (err["name"], err["line"], err["scope"])
                if key in variable_map:
                    variable_map[key]["issue"] = err["issue"]

            # Final list for display
            processed_variables = list(variable_map.values())

            # Format and display
            processor = ASTProcessor()
            header, column_widths, total_width = processor.generate_header(processed_variables)
            table_rows = processor.generate_table(processed_variables, column_widths, total_width)

            # Print the table and check pass/fail
            print("Variable Name Analysis:")
            print(header + table_rows)
            print("=" * 50)

            if "Variable" in header and "Scope" in header and "Line" in header and "Issue" in header:
                print("✅ Pass")
            else:
                print("❌ Fail")
                print(f" - Missing column header: 'Variable'")
                print(f" - Missing column header: 'Scope'")
                print(f" - Missing column header: 'Line'")
                print(f" - Missing column header: 'Issue'")


if __name__ == '__main__':
    unittest.main()
