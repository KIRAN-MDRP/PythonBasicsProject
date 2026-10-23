class Parent:
    __parentName = ""
    def __init__(self):
        self.__parentName = "MM.Satyanarayana"
    def getParentName(self):
        return self.__parentName
    def setParentName(self, name):
        self.__parentName = name

class Child(Parent):
    def __init__(self):
         # print(Parent.__parentName)
         pass
c = Child()
p = Parent()
# print(p.__parentName)