# Local Variable
def functionOne():
    functionOne = "Function One Local Variable"
    print(functionOne)
    globalVariable = "Global Variable Changed To functionOne Local Variable"
    print(globalVariable," from functionOne!")
    print(globals()['globalVariable']," from functionOne Second Time!")
def functionTwo():
    functionTwo = "Function Two Local Variable"
    print(functionTwo)
    print(globalVariable," from functionTwo!")
# Global Variable
globalVariable = "Global Variable"
functionOne()
functionTwo()