from numpy import ndarray

def separate_arrys():
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Single Row Array
noOfColumns = int(input("Enter the number of columns: "))
singleRowArray = ndarray(shape=(1, noOfColumns), dtype=int)
print("We are going to create a single row array with {} columns.".format(noOfColumns))
for columnvalue in range(noOfColumns):
    singleRowArray[0][columnvalue] = int(input("Enter the value for row {} and column {}: ".format(0,columnvalue)))
print("Single Row Array is: {}".format(singleRowArray))
separate_arrys()


# Single Column Array
noOfRows = int(input("Enter the number of rows: "))
print("We are going to create a single column array with {} rows.".format(noOfRows))
singleColumnArray = ndarray(shape=(noOfRows, 1), dtype=int)
for rowvalue in range(noOfRows):
    for columnvalue in range(1):
        singleColumnArray[rowvalue][columnvalue] = int(input("Enter the value for row {} and column {}: ".format(rowvalue,columnvalue)))
print("Single Column Array is: {}".format(singleColumnArray))
separate_arrys()

# Multi Dimension Array
noOfRows = int(input("Enter the number of rows: "))
noOfColumns = int(input("Enter the number of columns: "))
print("We are going to create a multi dimension array with {} rows and {} columns.".format(noOfRows,noOfColumns))
multiDimensionArray = ndarray(shape=(noOfRows, noOfColumns), dtype=int)
for rowvalue in range(noOfRows):
    for columnvalue in range(noOfColumns):
        multiDimensionArray[rowvalue][columnvalue] = int(input("Enter the value for row {} and column {}: ".format(rowvalue,columnvalue)))
print("Multi Dimension Array is: {}".format(multiDimensionArray))
separate_arrys()