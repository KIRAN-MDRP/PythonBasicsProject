# This program illustrates the basic data types and their conversions
# None data type
noneDataType = None

# Numeric data types
intDataType = 10
floatDataType = 3.14
complexDataType = complex(2,3)

# Boolean data types
booleanDataType = False

print("Initial value(s) of None data type is: ", noneDataType)
print("Initial value(s) of int, float and complex data types are: "
      , intDataType,",", floatDataType,",", complexDataType, " respectively!")

print("After converted int into float,complex and boolean data type: ")
intToFloatTypeConversion = float(intDataType)
intToComplexTypeConversion = complex(intDataType)
intToBooleanTypeConversion = bool(intDataType)
print(intToFloatTypeConversion,intToComplexTypeConversion,intToBooleanTypeConversion)

print("After converted float into int and complex data types: ")
floatToIntTypeConversion = int(floatDataType)
print(floatToIntTypeConversion)
#floatToComplexTypeConversion = complex(floatDataType)

print("After converted complex into int and float data types: ")
complexToIntTypeConversion = int(complexDataType.real)
complexToFloatTypeConversion = float(complexDataType.real)
print(complexToIntTypeConversion,complexToFloatTypeConversion)

booleanToIntTypeConversion = int(booleanDataType)
print("After converted bool into int data type: ", booleanToIntTypeConversion)


