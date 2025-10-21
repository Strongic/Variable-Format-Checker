'''Test Case 1: Global and Local Variables
---------------------------------------
'''
count = 10
def func():
    x = 5
    y = 6
'''
Test Case 2: Global Keyword Inside Function
-------------------------------------------
'''
def func():
    global total
    total = 100

'''Test Case 3: Incorrect Naming (CamelCase, Leading Caps, etc.)
--------------------------------------------------------------
'''
BadVarName = 1
def anotherFunc():
    camelCase = 5
    UPPER_case = 20

'''Test Case 4: Constants
----------------------
'''
MAX_SIZE = 50
min_value = 10

'''Test Case 5: Function & Class Naming
------------------------------------
'''
def ProcessData():
    pass

class myclass:
    pass

'''Test Case 6: Global-Like Variable in Function Without Keyword
--------------------------------------------------------------
'''
def something():
    config_var = 999  # not declared with `global`, should still be local

'''Test Case 7: Nested Functions
-----------------------------'''
def outer():
    a = 1
    def inner():
        b = 2

'''Test Case 8: Shadowing Variables
--------------------------------'''
x = 10
def f():
    x = 5  # local, shadows global x

'''Test Case 9: Multiple Assignment / Tuple Unpacking
--------------------------------------------------'''
a, b = 1, 2
def unpacker():
    x, y = (3, 4)

'''Test Case 10: Annoying but Valid Edge Cases
-------------------------------------------'''
def f():
    __weird__ = 5
    _temp = 2
    __ = 3

'''Test Case 11: Class Attributes vs Local Vars
--------------------------------------------'''
class Thing:
    CONSTANT = 42
    def __init__(self):
        self.value = 5
        temp = 10

'''Test Case 12: With Statements / Loops
-------------------------------------'''
for Index in range(10):
    print(Index)

with open('file.txt') as FileHandler:
    pass