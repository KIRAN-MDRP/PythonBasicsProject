# This program illustrates how to convert a tuple into list and string and vice versa


tupleInput = 'K','I','R','A','N'
print("Given tuple is: ", tupleInput)

# Tuple to String Conversion
stringOutput = "".join(tupleInput)
print("After converting into String is: ", stringOutput)

# String to Tuple Conversion
tupleOutputFromString = tuple(stringOutput)
print("After converting String into tuple is: ", tupleOutputFromString)

# Tuple to List
listOutput = list(tupleInput)
print("After converting into list is: ", listOutput)
print(type(listOutput))

# List to Tuple
tupleOutputFromString = tuple(listOutput)
print("After converting into tuple is: ", tupleOutputFromString)
print(type(tupleOutputFromString))
