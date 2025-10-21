"""
Takes in .py files and extracts variable information as follows:

INPUT:

count = 10
global x
def func():
    x = 5
    y = 6
    count = 20

REETURNS:

{'name': 'count', 'line': 1, 'scope': 'global'}
{'name': 'x', 'line': 2, 'scope': 'global'}
{'name': 'x', 'line': 4, 'scope': 'local'}
{'name': 'y', 'line': 5, 'scope': 'local'}
{'name': 'count', 'line': 6, 'scope': 'local'}

"""

import ast

class VariableExtractor(ast.NodeVisitor):
    def __init__(self):
        self.variables = []
        self.current_function = None

    # Assignment variables:
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.variables.append({
                    "name": target.id,
                    "line": node.lineno,
                    "scope": "local" if self.current_function else "global"
                })
        self.generic_visit(node)

    # Function Variables:
    def visit_FunctionDef(self, node):

        old_function = self.current_function
        self.current_function = node.name

        for arg in node.args.args:
            self.variables.append({
                    "name": arg.arg,
                    "line": arg.lineno,
                    "scope": "local"
                })
        self.generic_visit(node)

        self.current_function = old_function
        
    # Global Variables
    def visit_Global(self, node):
        for name in node.names:
            self.variables.append({
                    "name": name,
                    "line": node.lineno,
                    "scope": "global"
                })
        self.generic_visit(node)

    #extract
    def extract(self, code):
        self.variables = []
        tree = ast.parse(code)
        self.visit(tree)
        return self.variables

if __name__ == "__main__":
    with open("input.py", "r") as file:
        code = file.read()
    extractor = VariableExtractor()
    results = extractor.extract(code)

    """Print results in console"""
    # for var in results:
    #     print(var)