class Parent:
    def __init__(self):
        self.parentName = input("Enter parent name: ")

    def getParentName(self):
        return self.parentName

class ElderSon(Parent):
    def __init__(self):
        super().__init__()
        self.elderSonName = input("Enter elder son name: ")

    def getElderSonName(self):
        print("{} is the elder son of {}".format(self.elderSonName, self.getParentName()))

class SecondElderSon(Parent):
    def __init__(self):
        super().__init__()
        self.secondElderSonName = input("Enter second elder son name: ")

    def getSecondElderSonName(self):
        print("{} is the second elder son of {}".format(self.secondElderSonName, self.getParentName()))

elderSon = ElderSon()
elderSon.getElderSonName()

secondElderSon = SecondElderSon()
secondElderSon.getSecondElderSonName()
