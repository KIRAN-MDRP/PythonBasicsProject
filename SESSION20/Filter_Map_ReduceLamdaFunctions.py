import math
from functools import reduce

list1 = [None,1,2,3.4,complex(2,6),True]
list2 = ["KiranKumar Mandarapu","Surya Kumar Pedapudi","SatishKumar Mandarapu","VijayaShankar Varada"]

#Generate integer only list from the above list through filter
list_Only_Integer = list(filter(lambda x: isinstance(x, int), list1))
print(list_Only_Integer)

#Generate list of names whose surname is only Mandarapu.
list_Only_Mandarapu_Surname = list(filter(lambda name: name.endswith("Mandarapu"), list2))
print(list_Only_Mandarapu_Surname)

# Generate the Square of given number.
def getSquare(number):
    return int(math.pow(number,2))

# Map() lambda expression.
list3 = [23,1,45,32,15]
print("Initial list3 is: {}".format(list3))
print("After applied map lambda expression updated list3 is: \n {}".format(list(map(getSquare, list3))))
print("Square of each element through lambda expression is: \n {}".format(list(map(lambda x: int(math.pow(x,2)), list3))))

# Reduce() lambda Expression
list4 = [2,4,1,6,7,9]
print("Initial list4 is: {}.".format(list4))
print("Sum of given numbers from list4 is: {}.".format(reduce(lambda a,b: a+b, list4)))
print("Cumulative Multiplication of all numbers from given list4 is: {}".format(reduce(lambda a,b: a*b, list4)))

list5 = range(1,11)
outputDictionary = {"even":[], "odd":[]}
outputDictionary.get("even").extend(list(filter(lambda x: x % 2 == 0, list5)))
outputDictionary.get("odd").extend(list(filter(lambda x: x % 2 != 0, list5)))
print(outputDictionary)