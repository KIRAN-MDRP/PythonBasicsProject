# This program demonstrates the use of encapsulation concept.
class EncapsulationDemo:
    publicVariable = 10
    _protectedVariable = 20
    __privateVariable = 30

    def __init__(self):
        print("From Constructor: public, protected and private variables are: {}, {}, {} respectively!"
              .format(self.publicVariable, self._protectedVariable, self.__privateVariable))

    def displayVariables(self):
        print("From displayVariables: public, protected and private variables are: {}, {}, {} respectively!"
              .format(self.publicVariable, self._protectedVariable, self.__privateVariable))

ecd = EncapsulationDemo()
ecd.displayVariables()
ecd.__privateVariable = 40
ecd.displayVariables()