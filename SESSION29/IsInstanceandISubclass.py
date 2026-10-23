class ParentOne:
    def __init__(self):
        print("ParentOne Constructor")

class ParentTwo:
    def __init__(self):
        print("ParentTwo Constructor")

class ChildOne(ParentTwo):
    def __init__(self):
        print("ChildOne Constructor")

child = ChildOne()
print(isinstance(child, ChildOne))
print(isinstance(child, ParentTwo))
print(isinstance(child, ParentOne))
print(issubclass(ChildOne, ParentTwo))
print(issubclass(ChildOne, ParentOne))



