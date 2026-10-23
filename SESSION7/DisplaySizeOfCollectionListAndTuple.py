# This program illustrates to display the memory occupied by collections such as list and tuple etc
import sys
listInput = [1,2]
tupleInput = [1,2]

print("Size of list is: ", sys.getsizeof(listInput))
print("Size of tuple is: ", sys.getsizeof(tupleInput))