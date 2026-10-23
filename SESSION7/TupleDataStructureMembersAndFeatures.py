# This program demonstrates the tuple data structure members and features
# 1) Tuple is the ordered collection of Heterogenious elements.
# 2) Tuple is immutable. Once created, it cannot be modified.
# 3) Tuple allows duplicate elements.

tupleOne = ()
print("Empty tuple is: ", tupleOne)
print("Type of tupleOne is: ", type(tupleOne))
print("Features or Methods of tuple are: ", dir(tuple))
tupleTwo = (34,23.45,2+5J,None,False,26,26,26,34)
print("tupleTwo is: ", tupleTwo)

# Methods or Features of tuple are below.
# 1)count()
print("element 26 present in tupleTwo is: ", tupleTwo.count(26))

# 2)index()
print("Index of element 26 in tupleTwo is: ", tupleTwo.index(26))
print("Element present at position 0 is: ",tupleTwo[0])

# Iterate over tupleTwo and display elements one by one
print("TupleTwo elements in sequence are:")
for element in tupleTwo:
    print(element)
