# *****In python only operator overloading is possible. Not possible of Method and Constructor overloading.
# Overloading is nothing but method signature will be different but method name will be same.****

class One:
    def __init__(self):
        self.value = 1

    def __add__(self, other):
        return (self.value + other.value)

    
one = One()
two = One()
three = One()
print(one + two)
