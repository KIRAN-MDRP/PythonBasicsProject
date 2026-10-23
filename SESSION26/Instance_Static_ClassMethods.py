class Instance_Static_ClassMethods:
    staticVariable = "Static"
    def __init__(self):
        self.instanceVariable = "Instance"
        print("This is the constructor")
        print("{} from constructor".format(self.staticVariable))
        print("{} from constructor".format(self.instanceVariable))
        #print("{} from constructor".format(self.localVariable))

    def instanceMethod(self):
        print("This is an instance method")
        localVariable = "Local"
        print("{} from instance method".format(self.instanceVariable))
        print("{} from instance method".format(localVariable))
        print("{} from instance method".format(Instance_Static_ClassMethods.staticVariable))

    @staticmethod
    def staticMethod():
        print("This is a static method")
        print("{} from static method".format(Instance_Static_ClassMethods.staticVariable))


    @classmethod
    def classMethod(cls):
        print("This is a class method")
        print("{} from class method".format(Instance_Static_ClassMethods.staticVariable))
        print("{} from class method".format(cls.staticVariable))

objectOne = Instance_Static_ClassMethods()
objectOne.instanceMethod()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
Instance_Static_ClassMethods.staticMethod()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
Instance_Static_ClassMethods.classMethod()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("{} from outside class".format(Instance_Static_ClassMethods.staticVariable))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("{} from outside class".format(objectOne.staticVariable))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("{} from outside class".format(objectOne.instanceVariable))