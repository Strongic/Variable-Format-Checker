**Overview**

This project involves developing a Python static analysis tool that reads a Python script and verifies whether its variables follow correct naming conventions while also identifying their scope (global or local). The program will analyze the provided Python code, extract variable declarations, and classify them based on their scope while flagging any incorrectly formatted variable names.

**Objectives**

> Parse a given Python script and extract all variable declarations.

> Identify whether each variable is global or local.

> Verify that variable names adhere to Python naming conventions (e.g., snake_case for variables, uppercase for constants).

> Provide a summary report of identified variables, their scope, and any formatting violations.

**Key Features**
**1. Python Code Parsing**

> Use Python’s built-in Abstract Syntax Tree (AST) module to analyze the given script.

> Extract variable assignments, function parameters, and global declarations.

**2. Variable Scope Identification**

> Classify each variable as local (function scope) or global (script-wide scope).

> Detect global variables declared inside functions using the global keyword.

**3. Naming Convention Enforcement**

> Ensure variable names follow PEP 8 guidelines:

> Variable names should be lowercase with underscores (e.g., valid_variable_name).

> Constants should be in UPPERCASE_WITH_UNDERSCORES (e.g., MAX_VALUE).

> Class names should follow PascalCase (e.g., MyClass).

> Function names should be lowercase with underscores (e.g., process_data).

> Flag variable names that violate these conventions.

**4. Error Reporting & Output**

Generate a structured report listing:

> All variables, their name, scope (global/local), and line number.

> Naming convention violations with suggested corrections.

Output can be printed to the console or exported as a JSON/CSV file for further analysis.


**Example Input & Output**

**Sample Python Code Input:**

```
MAX_COUNT = 100  # Global constant

def my_function():
    x = 5  # Local variable
    global_var = 10  # Incorrect global declaration (not using 'global')

def another_function():
    global MAX_COUNT  # Using global variable
    tempVar = 20  # Incorrect naming (CamelCase instead of snake_case)
```

**Generated Output Report:**

```

Variable Name Analysis:
------------------------------------------------------
Variable         | Scope   | Line  | Issue
------------------------------------------------------
MAX_COUNT       | Global  | 1     | Should be UPPERCASE (Correct)
x              | Local   | 4     | Naming OK
global_var     | Local   | 5     | Warning: Global-like name but not declared global
MAX_COUNT      | Global  | 8     | Correct global usage
tempVar        | Local   | 9     | Naming Violation: Use snake_case (suggestion: temp_var)
------------------------------------------------------
```
