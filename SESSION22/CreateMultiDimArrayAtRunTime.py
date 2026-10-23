# This program illustrates how to create a multi-dimensional array at runtime
from numpy import *
noOfRows = int(input("Please enter the number of rows:"))
noOfColumns = int(input("Please enter the number of columns:"))
outputArray = ndarray(shape=(noOfRows,noOfColumns),dtype=int)
print("Please enter ",noOfRows*noOfColumns," elements into the array:")
for i in range(noOfRows):
    for j in range(noOfColumns):
        outputArray[i][j] = int(input("Please enter the element at row {} and column {} position: ".format(i,j)))
print("Array after adding elements is:", outputArray)