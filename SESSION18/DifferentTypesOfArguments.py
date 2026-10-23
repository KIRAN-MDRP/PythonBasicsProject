# There are four types of arguments.
# 1)Positional Arguments
# 2)Keyword Arguments
# 3)Default Arguments
# 4)Variable Length Arguments

def functionOne(firstName, middleName, lastName="Pedapudi"):
	print("First Name is: {}, Middle Name is: {} and Last Name is: {}.".format(firstName, middleName, lastName))

import math
def cumulativeMultipication(*multiple):
	print("The cumulative multiplication of given numbers is: {}".format(math.prod(multiple)))

# Only Positional Arguments Function Call
#functionOne("BalaBalaji","Mandarapu","KiranKumar")

# Only Keyword Arguments Function Call
#functionOne(middleName="BalaBalaji",lastName="Mandarapu",firstName="KiranKumar")

# Combination of Positional and Keyword Arguments Function Call
# **** While we used combination of positional and keyword arguments,
# the order of arguments matters. Positional arguments must come before keyword arguments.******
#functionOne("KiranKumar",lastName="Mandarapu",middleName="BalaBalaji")

# Default Arguments Function Call
#functionOne("KiranKumar",middleName="BalaBalaji")

# Variable Length Arguments Function Call
cumulativeMultipication(1,2,3,4,5)