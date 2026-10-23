# Built-In Functions
a = b= 10
print("a value is: ",a)
print("b value is: ",b)


# id() returns unique memory location of variables
print("id value of a is:",id(a))
print("id value of b is:",id(b))

# If we assigned same value for two different identifiers python allocate same memory locatioon
print(id(b))

# type() returns the class type of given object
print("Class type of ", a , "is: ", type(a))

# input() accepts value in runtime and stores into the variable
firstValue = float(input("Enter first value: "))
secondValue = float(input("Enter second value: "))
print("The sum of ", firstValue, " and ", secondValue, " is: ",int(firstValue+secondValue))

# help() returns the all functions of given object with explanation
listOne = [1,2,3]
print("Given list is: ", listOne)
print("help function returns below values ",help(listOne))

# dir() returns all the members and functions of given object
print("dir() of listOne is: \n", dir(listOne),end="")
