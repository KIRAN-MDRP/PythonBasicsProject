# This is a Python program to demonstrate the members and features of range data structure.
# Range is collection of numbers in a sequence
# It is immutable data structure. Once created, it cannot be modified.
# It is applicable only for sequence of number only

# Number of ways to create range()
# In two ways we can create range()
#     1) range(end)
#     2) range(start, end, step)

rangeOne = range(1,20)
print("Length of rangeOne is: ", len(rangeOne))
print("RangeOne elements in sequence are:")
for element in rangeOne:
    print(element, end=" ")
print("\n Type of rangeOne is: ", type(rangeOne))

rangeTwo = range(1,50,1)
print("Odd numbers those are present in first 50 integers are:")
for element in rangeTwo:
    print(element, end=" ")

rangeThree = range(0,50,2)
print("\n Even numbers those are present in first 50 integers are:")
for element in rangeThree:
    print(element, end=" ")

# Features or Methods of range() are:
print("\n Features of range()", dir(rangeOne))

# 1) count()
print("\n count of element 5 in rangeOne: ", rangeOne.count(5))

# 2) index()
print("\n index of element 5 in rangeOne: ", rangeOne.index(5))

# 3) start()
print("\n start of rangeOne: ", rangeOne.start)

# 4) stop()
print("\n stop of rangeOne: ", rangeOne.stop)

# 5) step()
print("\n step of rangeOne: ", rangeOne.step)


