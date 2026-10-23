# This file illustrates the operations of Set datastructure
# Set is the un ordered data structure
# Set allows to insert unique heterogenious elements
# It is mutable
# Duplicate elements insertion is not allowed

setOne = set()
setTwo = {36,35,21,42}
setThree = {45,34,56}
print("Initial setOne is: ", setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Set operations are: ", dir(setOne))
# Operations - There are totally 17 number of operations are there for set
# 01)add()        2)discard()     3)remove()     4)pop()    5)update()    6)copy()      7)union()       8)intersection() 9)intersection_update()  10)difference()
# 11)difference  12)symmetric    13)symmetric   14)clear() 15)disjoint() 16)isSubset() 17)isSuperset()
#     _update()     _difference()   _difference
#                                   _update()
# 9 Unique methods:
# add(),update(),copy(),discard(),remove(),clear(),pop(),union(),disjoint()
# 6 normal/_update methods:
# intersection(), difference(), symmetric_difference(), symmetric_difference_update(), difference_update(), intersection_update()
# 2 is___ methods:
# issubset(), issuperset()

# 1)add()
setOne.add(35)
setOne.add(42)
setOne.add(86)
setOne.add(26)
setOne.add(32)
print("Updated setOne is: ",setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# print("Length of the set is: ", len(setOne))
# print("Max elemnent of set is: ", max(setOne))
# print("Min elemnent of set is: ", min(setOne))
# print("Sum of all elements of set is: ", sum(setOne))

# 2)discard()
print("Before discard of 35 the setOne is: ", setOne)
setOne.discard(35)
print("After discarded 35 updated setOne is: ",setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# ***** Here in Set both discard() and remove() operations perform deletion a element from set.
# But the difference is remove() operation throws error if the element is not present in the set.
# Where as discard() operation does not throw error if the element is not present in the set. ******
# 3)remove()
print("Before remove 42 the setOne is: ", setOne)
setOne.remove(42)
print("After removed 42 updated set is: ",setOne)

# 4)pop() - It removes left most element from the given Set
# **** The same pop operation in list removed right most element where as
# here in set the removal operation happens from left most element. This is
# main difference here. ******
setOne.pop()
print("After popped  updated setOne is: ",setOne)
setOne.pop()
print("After popped again updated setOne is: ",setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
setOne.add(42)
setOne.add(86)
print("After adding 42 and 86 to setOne is: ",setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5)update()
setOne.update({1,2})
print("After updated setOne is: ",setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6)copy()
setFour = setOne.copy()
print("After copy setFour is:",setFour)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# discard operation
print("Before discard operation setFour is: ",setFour)
setFour.discard(42)
print("After discarded 42 set is: ", setFour)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# union, intersection, difference and symmetric_difference, difference_update, intersection_update
# and symmetric_difference_update operations
# 7) union()
print("Before union operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("setOne Union setTwo is::", setOne.union(setTwo))
print("setTwo Union setOne is::", setTwo.union(setOne))
print("After union operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 8) intersection()
print("Before Intersection operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("setOne Intersection setTwo is: ", setTwo.intersection(setOne))
print("setTwo Intersection setOne is: ",setTwo.intersection(setOne))
print("After Intersection operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 9) intersection_update()
print("Before Intersection_Update operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("setOne.intersection_update(setTwo): ", setOne.intersection_update(setTwo))
print("setTwo.intersection_update(setOne): ", setTwo.intersection_update(setOne))
print("After Intersection_Update operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 10)difference()
print("Before difference operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("setOne.difference(setTwo) is: ", setOne.difference(setTwo))
print("setTwo.difference(setOne) is: ", setTwo.difference(setOne))
print("After difference operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 11)difference_update()
print("Before difference_update operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("setOne.difference_update(setTwo) is: ", setOne.difference_update(setTwo))
print("setTwo.difference_update(setOne) is: ", setTwo.difference_update(setOne))
print("After difference operation setOne and setTwo are: ", setOne,"\n ",setTwo," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

setFive = {2,3,4,5,6}
# 12) symmetric_difference()
print("Before symmetrical_difference operation setFour and setFive are: ", setFour,"\n ",setFive," respectively")
print("setFour.symmetrical_difference(setFive) is: ", setFour.symmetric_difference(setFive))
print("setFive.symmetrical_difference(setFour) is: ", setFive.symmetric_difference(setFour))
print("After symmetrical_difference operation setFour and setFive are: ", setFour,"\n ",setFive," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 13) symmetric_difference_update()
print("Before symmetric_difference_update operation setFour and setFive are: ", setFour,"\n ",setFive," respectively")
print("setFour.symmetric_difference_update(setFive) is: ", setFour.symmetric_difference_update(setFive))
print("setFive.symmetric_difference_update(setFour) is: ", setFive.symmetric_difference_update(setFour))
print("After symmetric_difference_update operation setFour and setFive are: ", setFour,"\n ",setFive," respectively")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 14)clear()
print("Before clear operation setOne is: ", setOne)
setOne.clear()
print("After clear operation setOne is: ", setOne)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 15)disjoint()
print("setTwo is: ", setTwo)
setThree.add(42)
print("setThree is: ", setThree)
print("Is setTwo disjoint from setThree? ", setTwo.isdisjoint(setThree))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 16)isSubset()
print("Set Two is:", setTwo)
print("Set Three is: ", setThree)
print("Is setTwo subset of setThree? ", setTwo.issubset(setThree))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 17)isSuperset()
print("Is setThree superset of setTwo? ", setThree.issuperset(setTwo))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# frozenset()
# frozenset is the immutable version of set
frozenSetOne = frozenset({1,2,3})
frozenSetTwo = frozenset({4,5,6,3})
print("frozenSetOne is: ", frozenSetOne)
print("frozenSetTwo is: ", frozenSetTwo)
print("frozenSet features or methods are: ", dir(frozenSetOne))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# frozenSet features or methods
# frozenSet having 8 features or methods
# (union(),intersection(),difference(),symmetric_difference(),isdisjoint(),issubset(),issuperset(),copy())
# 5 Unique methods:
# union(),intersection(),difference(),symmetric_difference(),copy()
# 3 is_____ methods:
# isdisjoint(),issubset(),issuperset()
# 1)difference()
print("Before difference() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.difference(frozenSetTwo) is: ", frozenSetOne.difference(frozenSetTwo))
print("frozenSetTwo.difference(frozenSetOne) is: ", frozenSetTwo.difference(frozenSetOne))
print("After difference() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2)intersection()
print("Before intersection() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.intersection(frozenSetTwo) is: ", frozenSetOne.intersection(frozenSetTwo))
print("frozenSetTwo.intersection(frozenSetOne) is: ", frozenSetTwo.intersection(frozenSetOne))
print("After intersection() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3)union()
print("Before union() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.union(frozenSetTwo) is: ", frozenSetOne.union(frozenSetTwo))
print("frozenSetTwo.union(frozenSetOne) is: ", frozenSetTwo.union(frozenSetOne))
print("After union() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4)issubset()
print("Before issubset() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.issubset(frozenSetTwo) is: ", frozenSetOne.issubset(frozenSetTwo))
print("frozenSetTwo.issubset(frozenSetOne) is: ", frozenSetTwo.issubset(frozenSetOne))
print("After issubset() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5)issuperset()
print("Before issuperset() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.issuperset(frozenSetTwo) is: ", frozenSetOne.issuperset(frozenSetTwo))
print("frozenSetTwo.issuperset(frozenSetOne) is: ", frozenSetTwo.issuperset(frozenSetOne))
print("After issuperset() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6)isdisjoint()
print("Before isdisjoint() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.isdisjoint(frozenSetTwo) is: ", frozenSetOne.isdisjoint(frozenSetTwo))
print("frozenSetTwo.isdisjoint(frozenSetOne) is: ", frozenSetTwo.isdisjoint(frozenSetOne))
print("After isdisjoint() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7)symmetric_difference()
print("Before symmetric_difference() frozenSetOne and frozenSetTwo are: ", frozenSetOne, frozenSetTwo)
print("frozenSetOne.symmetric_difference(frozenSetTwo)", frozenSetOne.symmetric_difference(frozenSetTwo))
print("frozenSetTwo.symmetric_difference(frozenSetOne", frozenSetTwo.symmetric_difference(frozenSetOne))
print("After symmetric_difference() frozenSetOne and frozenSetTwo are: ",frozenSetOne, frozenSetTwo)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# 8) copy
print("Before copy() frozenSetOne is: ", frozenSetOne)
frozenSetThree = frozenSetOne.copy()
print("After copy() frozenSetOne and frozenSetThree are: ", frozenSetOne, frozenSetThree)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
