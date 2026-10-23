import copy
# This program illustrates the concept of Deep Copy and Shallow Copy of List Operations
listInput = [46,36,21,32,78,"KiranKumar Mandarapu"]
print("Given input list is: ", listInput)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Shallow copy of the list
listShallowCopy = listInput
print("After shallow copy original list is: {} and shallowcopylist is: {}".format(listInput,listShallowCopy))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Update the original list and shallow copy lists
listInput.append("Balaji")
listShallowCopy.append("Harish Kumar")
print("After updated original list by adding 'Balaji' is: {} and after updated shallowcopylist by adding 'Harish Kumar' is: {}".format(listInput,listShallowCopy))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

# Deep copy
listDeepCopy = copy.deepcopy(listInput)
print("After deep copy original list and deep copy list are: {} and {} respectively! ".format(listInput,listDeepCopy))
listInput.pop()
listDeepCopy.pop()
listDeepCopy.pop()
print("After remove elements through pop updated original list 'only one pop' and deepcopy 'two times pop' lists are: {} and {} respectively! ".format(listInput,listDeepCopy))



