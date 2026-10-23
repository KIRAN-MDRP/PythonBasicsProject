def singleDimensionalArrayElements(inputArray):
    for currentIndex in range(inputArray.size):
        print(inputArray[currentIndex], end=" ")
    print("&&&&&&&& End of the Single Dimensional Matrix &&&&&")

def multiDimensionalArrayElements(inputArray):
    for rowIndex in range(inputArray.shape[0]):
        for colIndsx in range(inputArray.shape[1]):
            print(inputArray[rowIndex][colIndsx], end=" ")
    print("&&&&&&&& End of the Multi Dimensional Matrix &&&&&")

def printSingleDimensioanlArrayFeatures(inputArray):
    print("Array is: {}".format(inputArray))
    print("dtype of Array is: {}".format(inputArray.dtype))
    print("ndim of Array is: {}".format(inputArray.ndim))
    print("shape of Array is: {}".format(inputArray.shape))
    print("size of Array is: {}".format(inputArray.size))
    print("Elements of Array are:")
    singleDimensionalArrayElements(inputArray)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def printMultiDimensioanlArrayFeatures(inputArray):
    print("Array is: {}".format(inputArray))
    print("dtype of Array is: {}".format(inputArray.dtype))
    print("ndim of Array is: {}".format(inputArray.ndim))
    print("shape of Array is: {}".format(inputArray.shape))
    print("size of Array is: {}".format(inputArray.size))
    print("Elements of Array are:")
    multiDimensionalArrayElements(inputArray)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
from numpy import array as ar
# Single Dimension Array (Single Row Only) Array
singleRowOnlyArray = ar([1, 2, 3, 4, 5])
printSingleDimensioanlArrayFeatures(singleRowOnlyArray)

# Single Dimension Array (Single Column Only) Array
singleColumnOnlyArray = ar([[1], [2], [3], [4], [5]])
printSingleDimensioanlArrayFeatures(singleColumnOnlyArray)

# Multi Dimensional (2 * 2) Array
twoDimensionalArray = ar([[1, 2], [3, 4]])
printMultiDimensioanlArrayFeatures(twoDimensionalArray)

# Multi Dimensional Array (3 * 3) Array
threeDimensionalArray = ar([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
printMultiDimensioanlArrayFeatures(threeDimensionalArray)

# Multi Dimensional Array (4 * 4) Array
fourDimensionalArray = ar([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
printMultiDimensioanlArrayFeatures(fourDimensionalArray)

# Multi Dimensional Array (4 * 3) Array
fourByThreeDimensionalArray = ar([[1, 2, 3], [6, 7, 8], [11, 12, 13], [16, 17, 18]])
printMultiDimensioanlArrayFeatures(fourByThreeDimensionalArray)

# Would like to flatten fourByThreeDimensionalArray
flattenedArray = fourByThreeDimensionalArray.flatten()
printSingleDimensioanlArrayFeatures(flattenedArray)

# Print Max and Min Elements of Entire Array and Row wise max, min elements Columnn wise max, min elements
print("Max Element of Entire Array is: {}".format(fourByThreeDimensionalArray.max()))
print("Min Element of Entire Array is: {}".format(fourByThreeDimensionalArray.min()))
print("Max Element of Column wise is: {}".format(fourByThreeDimensionalArray.max(axis=0)))
print("Min Element of Column wise is: {}".format(fourByThreeDimensionalArray.min(axis=0)))
print("Max Element of Row wise is: {}".format(fourByThreeDimensionalArray.max(axis=1)))
print("Min Element of Row wise is: {}".format(fourByThreeDimensionalArray.min(axis=1)))
