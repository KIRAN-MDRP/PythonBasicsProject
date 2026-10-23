# Single Dimension Array Creation through array module
from array import array as ar
int_Array_SingleDimension = ar('i',[1, 2, 3, 4, 5])
print("int Array Single Dimension is: {}".format(int_Array_SingleDimension))


# Single Dimension Array Creation At Runtime.
singleDimArrLength = int(input("Enter the length of single dimension array: "))
arrayAtRuntime = ar('i', [])
for currentIndex in range(singleDimArrLength):
    currentElement = int(input("Enter the element at index {}: ".format(currentIndex)))
    arrayAtRuntime.append(currentElement)
print("Array at runtime is: {}".format(arrayAtRuntime))
