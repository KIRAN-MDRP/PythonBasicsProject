# This program illustrates different ways of array creation through array module.
# There are totally six ways of array creation. Out of which through array() of array module
# and all remaining through numpy module we can create arrays.
# **** Through array module (array()) we can create single dimensional array only.
# Where as through numpy module we can create multi dimensional or single dimensional arrays.
# Using array module
# 1)array()
# Using Numpy module
# 2)linspace()
# 3)logspace()
# 4)arange()
# 5)zeros()
# 6)ones()

# Array Properties:
# There are 4 properties of array.
# 1)dtype - Represents the data type of the array.
# 2)ndim - Represents the number of dimensions of the array.
# 3)shape - Represents the shape of the array.
# 4)size - Represents the number of elements in the array.

# 1)array()
from array import array as arr
int_Array = arr('i', [1, 2, 3, 4, 5])

def printArrayProperties(inputArray):
    print("Data Type:", inputArray.dtype)
    print("Number of Dimensions:", inputArray.ndim)
    print("Shape:", inputArray.shape)
    print("Number of Elements:", inputArray.size)

def separator():
    print("--------------------------------------------------")

# Array Properties
#printArrayProperties(int_Array)

# 2)linspace()
from numpy import linspace
float_Array = linspace(2,10,6)
print("float Array is: {}".format(float_Array))
printArrayProperties(float_Array)
separator()


# 3)logspace
from numpy import logspace
logspace_Array = logspace(2,10,8)
print("logspace Array is: {}".format(logspace_Array))
printArrayProperties(logspace_Array)
separator()

# 4)arange()
from numpy import arange
arange_Array = arange(1,10,4)
print("arange Array is: {}".format(arange_Array))
printArrayProperties(arange_Array)
separator()

# 5)zeros()
from numpy import zeros
zeros_Array = zeros(10)
print("zeros Array is: {}".format(zeros_Array))
printArrayProperties(zeros_Array)
separator()

# 6)ones()
from numpy import ones
ones_Array = ones(10)
print("ones Array is: {}".format(ones_Array))
printArrayProperties(ones_Array)
separator()