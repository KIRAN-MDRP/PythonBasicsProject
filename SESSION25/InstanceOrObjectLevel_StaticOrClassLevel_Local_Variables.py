# This program demonstrates the difference between instance, class level variables and Local variables.
class AllKindOfVariables:
    classVariable = "Hai I am a class variable"

    def __init__(self):
        self.constructorInstanceVariable = "Hai I am an instance variable"
        constructorLocalVariable = "Hai I am a local variable from constructor"
        print(self.constructorInstanceVariable)
        print(constructorLocalVariable)

    def methodOne(self):
        self.MethodInstanceVariable = "Hai I am an instance variable from method"
        methodLocalVariable = "Hai I am a local variable from method"
        print(self.constructorInstanceVariable)
        print(methodLocalVariable)

akov = AllKindOfVariables()
akov.methodOne()


