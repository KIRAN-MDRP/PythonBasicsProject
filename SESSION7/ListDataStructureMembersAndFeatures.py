# This program illustrates the members and features of List data Structure
# List is the collection of Heterogenious data types
# There are totally 11 methods are available in list
# Features of List:
# 1) It allows duplicate elements
# 2) It is mutable data structure
# 3) It is ordered collection of elements
listOne = []
print("We can create emply list and created empty list is: ", listOne)
listOne = [4]
print("listOne with Single element is: ", listOne)

# Methods of list are below.
# 01.append(element) 2.copy() 3.count(element) 4.extend(datastructure) 5.pop() 6.index(element) 7.remove(element) 8.reverse() 9.sort() 10.insert(position, element)
# 11.clear()
print(dir(listOne))
print("Initial list and length of list is: ", listOne, len(listOne))

# 1.append(element)
listOne.append(10)
listOne.append(23.45)
listOne.append("Python")
listOne.append(2+3J)
listOne.append(None)
listOne.append(True)
print("List after appending elements and length of list is: ", listOne, "\n",len(listOne))

# 2.copy()
listTwo = listOne.copy()
print("List Two elements are: ", listTwo)

# 3.count(element)
listTwo.append("Python")
listTwo.append(10)
listTwo.append("Python")
print("Count of Python in listTwo is: ", listTwo.count("Python"))
print("Count of 10 in listTwo is: ", listTwo.count(10))

# 4.extend(datastructure)
print("List Two elements before extending with listThree: ", listTwo)
listThree = ["Maths","Physics","Chemistry"]
listTwo.extend(listThree)
print("After extending listTwo with listThree: ", listTwo)

# 5.pop()
# ***** Removes right most element from the list ************
print("List Two elements before poping: ", listTwo)
listTwo.pop()
print("List Two elements after poping: ", listTwo)

# 6.index(element)
print("Index of Python in listTwo is: ", listTwo.index("Python"))
print("Index of 10 in listTwo is: ", listTwo.index(10))

# 7.remove(element)
# ************ Removes first occurence of element from the list ************
print("List Two elements before removing Python: ", listTwo)
listTwo.remove("Python")
print("List Two elements after removing Python: ", listTwo)

# 8.reverse()
print("List Two elements before reversing: ", listTwo)
listTwo.reverse()
print("List Two elements after reversing: ", listTwo)

# 9.sort()
# ***** For both integers and String types we are having two types of sorted() *********
# sorted(datastructure) -- for ascending order
# sorted(datastructure, reverse=True) -- for descending order
listOnlyIntegers = []
for element in listTwo:
    if type(element) == int or type(element) == float:
        listOnlyIntegers.append(int(element))
print("listOnlyIntegers elements before sorting: ", listOnlyIntegers)
listOnlyIntegers.sort()
print("listOnlyIntegers elements after sorting: ", listOnlyIntegers)
# Using sorted(datastructure)
print("listOnlyIntegers elements after sorting: ", sorted(listOnlyIntegers))
print("listOnlyIntegers elements after sorting in reverse order: ", sorted(listOnlyIntegers, reverse=True))

# 10.insert(position, element)
print("List Two before element 36 insertion", listTwo)
listTwo.insert(3, 36)
print("List Two after element 36 insertion", listTwo)

# 11.clear()
print("List Two before clearing: ", listTwo)
listTwo.clear()
print("List Two after clearing: ", listTwo)

# del()
print("Before deletion listTwo is:", listTwo)
del(listTwo)








