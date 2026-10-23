# This program illustrates the concept of Arrays in Python
from array import *
firstArray = array('i',[1,2,3,4,5,6,7,8,9])
print("First array is:", firstArray)
print("Max element in first array is:", max(firstArray))
print("Min element in first array is:", min(firstArray))
print("Sum of all elements in first array is:", sum(firstArray))

# Dynamic one dimension array creation
sizeOfSecondArray = int(input("Enter size of second array: "))
secondArray = array('i',[])
for ele_index in range(sizeOfSecondArray):
    element = int(input("Enter element:"))
    secondArray.append(element)
print("Second array is:", secondArray)
searchElment = int(input("Enter element to be searched: "))
if searchElment in secondArray:
    print("Element ", searchElment, " is present in the second array at index ", secondArray.index(searchElment))
else:
    print("Element ", searchElment, " is not present in the second array")

arrayToList = list(firstArray)
print(arrayToList," and ", type(arrayToList))
