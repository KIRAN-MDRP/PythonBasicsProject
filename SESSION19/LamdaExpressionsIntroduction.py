#import SESSION20.Filter_Map_ReduceLamdaFunctions as fmrl
from SESSION20.Filter_Map_ReduceLamdaFunctions import getSquare as gs

# This program provide introduction to Lambda expressions


le1 = lambda:"Lambda expression with out any arguments and only print statement"
le2 = lambda inputName:"Entered name is: {}".format(inputName)
le3 = lambda input1,input2:"{} is greater than {}".format(input1,input2) if input1>input2 \
    else "{} is less than {}".format(input1,input2)
le4 = lambda input1,input2,input3:"{} is greater than {} and {}".format(input1,input2,input3) if (input1 > input2 and input1 > input3) else (
    "{} is greater than {} and {}".format(input2,input1,input3)) if input2 > input3 and input2 > input1 else (
    "{} is greater than {} and {}".format(input3,input2,input1))



print(le1())
print(le2("KiranKumar"))
print(le3(1,2))
print(le4(1,2,3))
print(gs(3))