import unittest
import VariableExtractor


def recognize_error(variable):
    """
    Recognizes if there is an issue with the variable's naming or scope.
    Returns an issue description (if any).
    """
    var_name = variable['name']
    scope = variable['scope']
    issue = None

    # Rule for local variables: they should use snake_case unless the name is a single character or follows snake_case correctly.
    if scope == "local":
        core_name = var_name.lstrip("_")

        # Ignore single character variable names
        if len(core_name) > 1 and not core_name.islower():
            # Check if there's any uppercase letter in the middle of the name (not the first character)
            if any(c.isupper() for c in core_name[1:]):
                issue = 'Naming Violation: Use snake_case'

    # Rule for global variables: they should use UPPERCASE_WITH_UNDERSCORES.
    else:
        if not var_name.isupper() or "__" in var_name:
            issue = 'Naming Violation: Use UPPERCASE_WITH_UNDERSCORES'

    return issue


def format_output(variables):
    """
    Formats the extracted variables and their issues into the required output string.
    """
    formatted_output = []

    for var in variables:
        issue = recognize_error(var)
        formatted_output.append(f"{var['name']} | {var['scope']} | {var['line']} | {issue if issue else 'None'}")

    return '\n'.join(formatted_output)


class TestVariableAnalysis(unittest.TestCase):
    def test_error_recognition(self):
        test_code = """
a = 10
b = 20
GLOBAL_VAR = 30
def my_func():
    LOCAL_VAR = 40
    x = 5
    y = 6
    z = 7
"""

        extractor = VariableExtractor.VariableExtractor()
        extracted_variables = extractor.extract(test_code)

        # Format the output
        formatted_actual_data = format_output(extracted_variables)

        expected_error_data = """a | global | 2 | Naming Violation: Use UPPERCASE_WITH_UNDERSCORES
b | global | 3 | Naming Violation: Use UPPERCASE_WITH_UNDERSCORES
GLOBAL_VAR | global | 4 | None
LOCAL_VAR | local | 6 | Naming Violation: Use snake_case
x | local | 7 | None
y | local | 8 | None
z | local | 9 | None
"""

        self.assertEqual(formatted_actual_data.strip(), expected_error_data.strip(),
                         f"\nFAIL: Error recognition mismatch.\nExpected:\n{expected_error_data}\nGot:\n{formatted_actual_data}")

        print(formatted_actual_data)

if __name__ == "__main__":
    unittest.main()
