# This program illustrates how to create Single Dimension Numpy array at Runtime
# We accept length of the array at runtime and insert elements at runtime
from numpy import *
noOfElements = int(input("Please enter the nuumber of elements of array:"))
print("Length of the array is:", noOfElements)
outputArray = ndarray(shape=(noOfElements,),dtype=int)
print("Initially array is:", outputArray)
print("Number of elements present in the array currently are:", len(outputArray))
print("Now insert ",noOfElements," the elements into the array:")
for i in range(noOfElements):
    currentElement = int(input("Please enter the element to be added: "))
    outputArray[i] = currentElement
outputArray = array(outputArray)
print("Array after adding elements is:", outputArray)
print(type(outputArray))
print("Number of elements present in the array is:", len(outputArray))