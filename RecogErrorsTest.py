test_variables = [
    {"name": "x", "line": 3, "scope": "local", "expected": {"issue": None, "after": "x"}},
    {"name": "MAX_COUNT", "line": 1, "scope": "global", "expected": {"issue": None, "after": "MAX_COUNT"}},
    {"name": "totalValue", "line": 5, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "total_value"}},
    {"name": "user_name", "line": 6, "scope": "local", "expected": {"issue": None, "after": "user_name"}},
    {"name": "DEBUG_MODE", "line": 2, "scope": "global", "expected": {"issue": None, "after": "DEBUG_MODE"}},
    {"name": "debug_mode", "line": 7, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "DEBUG_MODE"}},
    {"name": "NumItems", "line": 8, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "num_items"}},
    {"name": "config", "line": 9, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "CONFIG"}},
    {"name": "is_valid", "line": 10, "scope": "local", "expected": {"issue": None, "after": "is_valid"}},
    {"name": "_temp", "line": 11, "scope": "local", "expected": {"issue": None, "after": "_temp"}},
    {"name": "MAXSPEED", "line": 12, "scope": "global", "expected": {"issue": None, "after": "MAXSPEED"}},
    {"name": "invalid-name", "line": 13, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "invalid_name"}},
    {"name": "AnotherVar", "line": 14, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "another_var"}},
    {"name": "another_var", "line": 15, "scope": "local", "expected": {"issue": None, "after": "another_var"}},
    {"name": "CONSTANT1", "line": 16, "scope": "global", "expected": {"issue": None, "after": "CONSTANT1"}},
    {"name": "constant_2", "line": 17, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "CONSTANT_2"}},
    {"name": "snake_case_good", "line": 18, "scope": "local", "expected": {"issue": None, "after": "snake_case_good"}},
    {"name": "ThisIsPascal", "line": 19, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "this_is_pascal"}},
    {"name": "ALLCAPS", "line": 20, "scope": "global", "expected": {"issue": None, "after": "ALLCAPS"}},
    {"name": "VeryLongVariableNameThatShouldBeSnakeCase", "line": 22, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "very_long_variable_name_that_should_be_snake_case"}},
    {"name": "max_value", "line": 23, "scope": "local", "expected": {"issue": None, "after": "max_value"}},
    {"name": "MAX_VALUE", "line": 24, "scope": "global", "expected": {"issue": None, "after": "MAX_VALUE"}},
    {"name": "__internal", "line": 25, "scope": "local", "expected": {"issue": None, "after": "__internal"}},
    {"name": "UPPERCASE123", "line": 26, "scope": "global", "expected": {"issue": None, "after": "UPPERCASE123"}},
    {"name": "global_var", "line": 27, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "global_var"}},
    {"name": "is_global", "line": 28, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "is_global"}},
    {"name": "non_global", "line": 29, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "non_global"}},
    {"name": "myglobalvalue", "line": 30, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "MYGLOBALVALUE"}},
    {"name": "globalSetting", "line": 31, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "global_setting"}},
    {"name": "GLOBAL_COUNTER", "line": 32, "scope": "global", "expected": {"issue": None, "after": "GLOBAL_COUNTER"}},
    {"name": "global_constant", "line": 33, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "GLOBAL_CONSTANT"}},
    {"name": "gLoBaL", "line": 34, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "GLOBAL"}},
    {"name": "GlobalValue", "line": 35, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "global_value"}},
    {"name": "hasGlobalScope", "line": 36, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "has_global_scope"}},
    {"name": "GLOBAL_CONSTANT", "line": 37, "scope": "global", "expected": {"issue": None, "after": "GLOBAL_CONSTANT"}},
    {"name": "some_var", "line": 38, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "SOME_VAR"}},
    {"name": "_hiddenGlobal", "line": 39, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "_hidden_global"}},
    {"name": "anotherGlobalThing", "line": 40, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "another_global_thing"}},
    {"name": "temp", "line": 41, "scope": "local", "expected": {"issue": None, "after": "temp"}},
    {"name": "TempVar", "line": 42, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "temp_var"}},
    {"name": "MAX_TEMP", "line": 43, "scope": "global", "expected": {"issue": None, "after": "MAX_TEMP"}},
    {"name": "maxTemp", "line": 44, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "MAX_TEMP"}},
    {"name": "configSettings", "line": 45, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "config_settings"}},
    {"name": "CONFIG_SETTINGS", "line": 46, "scope": "global", "expected": {"issue": None, "after": "CONFIG_SETTINGS"}},
    {"name": "hiddenVar", "line": 47, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "hidden_var"}},
    {"name": "__HIDDEN_CONST", "line": 48, "scope": "global", "expected": {"issue": "Naming Violation: Use UPPERCASE_WITH_UNDERSCORES", "after": "HIDDEN_CONST"}},
    {"name": "_private_var", "line": 49, "scope": "local", "expected": {"issue": None, "after": "_private_var"}},
    {"name": "_PrivateVar", "line": 50, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "_private_var"}},
    {"name": "numberOfItems", "line": 51, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "number_of_items"}},
    {"name": "NUMBER_OF_ITEMS", "line": 52, "scope": "global", "expected": {"issue": None, "after": "NUMBER_OF_ITEMS"}},
    {"name": "loadConfigFile", "line": 53, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "load_config_file"}},
    {"name": "IS_ENABLED", "line": 54, "scope": "global", "expected": {"issue": None, "after": "IS_ENABLED"}},
    {"name": "globalData", "line": 55, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "global_data"}},
    {"name": "DATA_GLOBAL", "line": 56, "scope": "global", "expected": {"issue": None, "after": "DATA_GLOBAL"}},
    {"name": "global_status", "line": 57, "scope": "local", "expected": {"issue": "Suspicious: name includes 'global', but is local", "after": "global_status"}},
    {"name": "updateValue", "line": 58, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "update_value"}},
    {"name": "valueUpdated", "line": 59, "scope": "local", "expected": {"issue": "Naming Violation: Use snake_case", "after": "value_updated"}},
    {"name": "RESET_FLAG", "line": 60, "scope": "global", "expected": {"issue": None, "after": "RESET_FLAG"}},
]

from RecognizeErrors import recognizeErrors

def test_variable_naming():
    actual_errors = recognizeErrors(test_variables)
    actual_lookup = {error['line']: error for error in actual_errors}
    failed = False

    for var in test_variables:
        line = var["line"]
        expected_issue = var["expected"]["issue"]
        actual_issue = actual_lookup.get(line, {}).get("issue")

        if expected_issue != actual_issue:
            failed = True
            print(f"[FAIL] Line {line} - Name: {var['name']}")
            print(f"  Expected Issue: {expected_issue}, Actual Issue: {actual_issue}")
        else:
            print(f"[PASS] Line {line} - {var['name']}")

    if not failed:
        print("\n✅ All tests passed.")
    else:
        print("\n❌ Some tests failed.")

test_variable_naming()
