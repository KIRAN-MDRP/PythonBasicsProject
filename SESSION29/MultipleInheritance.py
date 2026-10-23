class ParentOne:
    def __init__(self):
        print("ParentOne Constructor")

    def methodOne1(self):
        print("ParentOne Method One")

    def methodTwo1(self):
        print("ParentOne Method Two")

class ParentTwo:
    def __init__(self):
        print("ParentTwo Constructor")

    def methodOne(self):
        print("ParentTwo Method One")

    def methodTwo(self):
        print("ParentTwo Method Two")

class ChildOne(ParentOne, ParentTwo):

    def __init__(self):
        print("ChildOne Constructor")

c = ChildOne()
c.methodOne()
c.methodTwo()