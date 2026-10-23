# This program illustrates the concept of numpy array creation and its features
# Using numpy arrays we can create single dimension and multi dimension arrays
# numpy Arrays having below properties such as
# dtype - returns data type of given array
# ndim - dimensions of given array
# shape - rows and column numbers of given array
# size - No of elements from given array
from numpy import *

# Single dimension arrays using numpy package
singleDimArray = array([36,35,45,85])
print("Given single dimension array is:", singleDimArray)
print("Data type of singleDimArray is:", singleDimArray.dtype)
print("Dimensions of singleDimArray is:", singleDimArray.ndim)
print("Shape of singleDimArray is:", singleDimArray.shape)
print("Number of elements in singleDimArray are:", singleDimArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Single Row Array
mulDimSingleRowArray = array([[1,2,3,4,5]])
print("Given Single Row array is:", mulDimSingleRowArray)
print("Data type of mulDimSingleRowArray is:", mulDimSingleRowArray.dtype)
print("Dimensions of mulDimSingleRowArray is:", mulDimSingleRowArray.ndim)
print("Shape of mulDimSingleRowArray is:", mulDimSingleRowArray.shape)
print("Number of elements in mulDimSingleRowArray are:", mulDimSingleRowArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Single column array
mulDimSingleColArray = array([[36],[25],[12]])
print("Given Single Column array is:", mulDimSingleColArray)
print("Data type of singleDimColArray is:", mulDimSingleColArray.dtype)
print("Dimensions of singleDimColArray is:", mulDimSingleColArray.ndim)
print("Shape of singleDimColArray is:", mulDimSingleColArray.shape)
print("Number of elements in singleDimColArray are:", mulDimSingleColArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Two by Two multi dimension array
twoByTwoArray = array([[1,2],[3,4,]])
print("Given Two By Two array is:", twoByTwoArray)
print("Data type of twoByTwoArray is:", twoByTwoArray.dtype)
print("Dimensions of twoByTwoArray is:", twoByTwoArray.ndim)
print("Shape of twoByTwoArray is:", twoByTwoArray.shape)
print("Number of elements in twoByTwoArray are:", twoByTwoArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Three by Three multi dimension array
threeByThreeArray = array([[1,2,3],[4,5,6],[7,8,9]])
print("Given Three By Three Array is:", threeByThreeArray)
print("Data type of threeByThreeArray is:", threeByThreeArray.dtype)
print("Dimensions of threeByThreeArray is:", threeByThreeArray.ndim)
print("Shape of threeByThreeArray is:", threeByThreeArray.shape)
print("Number of elements in threeByThreeArray are:", threeByThreeArray.size)
print("Max element in threeByThreeArray is:", threeByThreeArray.max())
print("Min element in threeByThreeArray is:", threeByThreeArray.min())
print("Row wise max elements list in threeByThreeArray is:", threeByThreeArray.max(axis=1))
print("Row wise min element list in threeByThreeArray is:", threeByThreeArray.min(axis=1))
print("Column wise max element list in threeByThreeArray is:", threeByThreeArray.max(axis=0))
print("Column wise min element list in threeByThreeArray is:", threeByThreeArray.min(axis=0))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# ***** Among all elments from array if atleast is float that integer array will become float array
intArray = array([[1,2],[2.3,5]])
print("Given Int Array is:", intArray)
print("Data type of intArray is:", intArray.dtype)
print("Dimensions of intArray is:", intArray.ndim)
print("Shape of intArray is:", intArray.shape)
print("Number of elements in intArray are:", intArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# If we wants the above array to be represented as only int we can make use of dtype = 'int'
pureIntArray = array(intArray,dtype=int)
print("Given Pure Int Array is:", pureIntArray)
print("Data type of pureIntArray is:", pureIntArray.dtype)
print("Dimensions of pureIntArray is:", pureIntArray.ndim)
print("Shape of pureIntArray is:", pureIntArray.shape)
print("Number of elements in pureIntArray are:", pureIntArray.size)
# We can flatten two dimension array into one dimension array using flatten()
convertTwoIntoSingleDimArray = pureIntArray.flatten()
print("Given flatten Int Array is:", convertTwoIntoSingleDimArray)
print("Data type of flatten Int Array is:", convertTwoIntoSingleDimArray.dtype)
print("Dimension of flatten Int Array is: ", convertTwoIntoSingleDimArray.ndim)
print("Shape of flatten Int Array is:", convertTwoIntoSingleDimArray.shape)
print("Number of elements in flatten Int Array are:", convertTwoIntoSingleDimArray.size)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Array creation using matlab methods
# We have below matlab methods such as linspace(), logspace(), arange(), zeros(), ones()
arrayThroughlinSpace = linspace(1,30,12)
print("Given linspace array is:", arrayThroughlinSpace)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

arrayThroughLogSpace = logspace(1,3,12)
print("Given logspace array is:", arrayThroughLogSpace)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

arrayThroughArange = arange(1,30,5)
print("Given Arange array is:", arrayThroughArange)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

arrayThroughZeros = zeros((5,3),dtype=int)
print("Given Zeros array is:", arrayThroughZeros)
print("Given zeros array is:", arrayThroughZeros)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

arrayThroughNumbers = ones((3,5),dtype=int)
print("Given numbers array is:", arrayThroughNumbers)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")





