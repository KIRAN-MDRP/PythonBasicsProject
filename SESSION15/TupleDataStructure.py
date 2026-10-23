# This program illustrates basic functionalities of tuple datastructure
# Tuple with single element
tupleOne = 2,
print("Tuple with single value: ",tupleOne)
print("Tuple of tupleOne is: ",type(tupleOne))

# Tuple with multiple elements
tupleTwo = "Kiran",2,45.6,True
print("Tuple with multiple values is: ",tupleTwo)

# We cannot modify tuple once its created.
# tupleTwo[0] = "KiranKumar"
# print("Updated Tuple is: ",tupleTwo)

# Get Tuple members and functions through dir()
print("Tuple members and functions are: ",dir(tupleTwo))

# Tuple with multiple and repeated values
tupleWithMultipleAndRepeatedValues = ("Mandarapu",23,2,2,3,3,4,4,5,6,7)

# Tuple functions
# Count function
print("Number 2 count value is: ", tupleWithMultipleAndRepeatedValues.count(2))

# Index function
print("Index of the 3 is: ",tupleWithMultipleAndRepeatedValues.index(3))
print("Length of the given tuple is: ", len(tupleWithMultipleAndRepeatedValues))
