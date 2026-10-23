# This program demonstrates all the operators in Python
# There are 34 no. of operators are there in Python which are categorized into 7 groups.
# 1)Arithmetic Operators (7)
# 2)Relational Operators (6)
# 3)Assignment Operators (8)
# 4)Logical Operators (3)
# 5)Membership Operators(2)
# 6)Identity Operators(2)
# 7)Bitwise Operators(7)

# 1) Arithmetic Operators
# There are 7 arithmetic operators in Python.
# Such as Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, Floor Division etc.
# 1.1 Addition
print("++++++++++++++++ Arithmetic Operators (7) Start  +++++++++++++++++")
firstIntValue = int(input("Enter the first integer value: "))
secontIntValue = int(input("Enter the second integer value: "))
print("Addition of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue+secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.2 Subtraction
print("Subtraction of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue-secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.3 Multiplication
print("Multiplication of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue*secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.4 Division
print("Division of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue/secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.5 Floor Division
print("Floor Division of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue//secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.6 Modulus
print("Modulus of {} {} is: {} ".format(firstIntValue, secontIntValue,(firstIntValue%secontIntValue)))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 1.7 Exponentiation
groundValue = int(input("Please enter the groud integer value:"))
powerIntValue = int(input("Please enter the power integer value:"))
print("Exponentiation value {} to the power of {} is: {} ".format(groundValue,powerIntValue,(groundValue**powerIntValue)))
print("++++++++++++++ Arithmetic Operators End! +++++++++++++++++++++++++")

# 2 Relational Operators (6)
print("++++++++++++++++ Relational Operators (6) Start  +++++++++++++++++")
# 2.1 < Operator
print("Is 2 < 3?", 2 < 3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2.2 > Operator
print("Is 2 > 3?", 2 > 3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2.3 <= Operator
print("Is 2 <= 3?", 2 <= 3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2.4 >= Operator
print("Is 2 >= 3?", 2 >= 3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2.5 == Operator
print("Is 2 == 3?", 2 == 3)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2.6 != Operator
print("Is 2 != 3?", 2 != 3)
print("+++++++++++++ Relational Operators End! +++++++++++++++++++++++++")
#
# 3. Assignment Operators (8)
print("+++++++++++++ Assignment Operators (8) Start! ++++++++++++++++++++")

# 3.1 = (Assignment) Operator
firstAssignmentInput = 4
print("firstInput value is:", firstAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.2 += (Add and Assign) Operator
secondAssignmentInput = 5
print("Initial value of secondInputvalue is:", secondAssignmentInput)
secondAssignmentInput += 1
print("After incremented by 1 updated secondInputvalue value is:", secondAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.3 -= (Subtract and Assign) Operator
thirdAssignmentInput = 6
print("Initial value of thirdInputvalue is:", thirdAssignmentInput)
thirdAssignmentInput -= 1
print("After decremented by 1 updated thirdInputvalue value is:", thirdAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.4 *= (Multiply and Assign) Operator
fourthAssignmentInput = 7
print("Initial value of fourthInputvalue is:", fourthAssignmentInput)
fourthAssignmentInput *= 2
print("After multiplied by 2 updated fourthInputvalue value is:", fourthAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.5 /= (Divide and Assign) Operator
fifthAssignmentInput = 8
print("Initial value of fifthInputvalue is:", fifthAssignmentInput)
fifthAssignmentInput /= 2
print("After divided by 2 updated fifthInputvalue value is:", fifthAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.6 %= (Modulus and Assign) Operator
sixthAssignmentInput = 9
print("Initial value of sixthInputvalue is:", sixthAssignmentInput)
sixthAssignmentInput %= 2
print("After modulus by 2 updated sixthInputvalue value is:", sixthAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.7 //= (Floor Division and Assign) Operator
seventhAssignmentInput = 10
print("Initial value of seventhInputvalue is:", seventhAssignmentInput)
seventhAssignmentInput //= 2
print("After floor division by 2 updated seventhInputvalue value is:", seventhAssignmentInput)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3.8 **= (Exponent and Assign) Operator
eighthAssignmentInput = 2
print("Initial value of eighthInputvalue is:", eighthAssignmentInput)
eighthAssignmentInput **= 3
print("After exponent by 3 updated eighthInputvalue value is:", eighthAssignmentInput)
print("++++++++++++++++ Assignment Operators End! ++++++++++++++++++++++++")
#
# 4.Logical Operators (3)
# 4.1 and operator
print("++++++++++++++++ Logical Operators (3) Start! ++++++++++++++++++++++++")
print(" 2 < 3 and 4 > 1", 2 < 3 and 4 > 1)
print(" 2 > 3 and 4 > 1", 2 > 3 and 4 > 1)
print(" 2 < 3 and 4 < 1", 2 < 3 and 4 < 1)
print(" 2 > 3 and 4 < 1", 2 > 3 and 4 < 1)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4.2 or operator
print(" 2 < 3 or 4 > 1", 2 < 3 or 4 > 1)
print(" 2 > 3 or 4 > 1", 2 > 3 or 4 > 1)
print(" 2 < 3 or 4 < 1", 2 < 3 or 4 < 1)
print(" 2 > 3 or 4 < 1", 2 > 3 or 4 < 1)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4.3 not operator
LogicalOperatorsList = [1,2,3]
print("5 not in LogicalOperatorsList", 5 not in LogicalOperatorsList)
print("1 in LogicalOperatorsList", 1 in LogicalOperatorsList)
print("not(True)", not(True))
# print("++++++++++++++++++ Logical Operators End! +++++++++++++++++++++++++++")

# 5 Membership Operators (2)
# 5.1 in operator
print(" 1 in LogicalOperatorsList", 1 in LogicalOperatorsList)
print(" 5 in LogicalOperatorsList", 5 in LogicalOperatorsList)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5.2 not in operator
print(" 1 not in LogicalOperatorsList", 1 not in LogicalOperatorsList)
print(" 5 not in LogicalOperatorsList", 5 not in LogicalOperatorsList)
print("++++++++++++++++++++ Membership Operators End! +++++++++++++++++++++++")

# 6 Identity Operators(2)
# 6.1 is operator
identityFirstIniput = identitySecondInput = 4
print("identityFirstIniput is identitySecondInput", identityFirstIniput is identitySecondInput)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6.2 is not operator
identityThirdInput =  4
identityFourthInput = 9
print("identityFirstIniput is not identitySecondInput", identityFirstIniput is not identitySecondInput)
print("identityThirdIniput is not identityFourthInput", identityThirdInput is not identityFourthInput)
print("++++++++++++++++++++ Identity Operators End! ++++++++++++++++++++++++++")

# 7 Bitwise Operators(6)
# AND(&), OR(|), XOR(^), NOT(~), LEFTSHIFT(<<), RIGHTSHIFT(>>)
# 7.1 AND (&) operator
#   n1    n2      result
#   1     0        0
#   0     1        0
#   0     0        0
#   1     1        1
print("+++++++++++++++++++++ Bitwise Operators Start +++++++++++++++++++++++++")
print("Binary form of 2 is: ", bin(2))
print("Binary form of 3 is: ", bin(3))
print(" 2 & 3", 2 & 3)
print("Binary form of 15 is: ", bin(15))
print("Binary form of 36 is: ", bin(36))
print(" 15 & 36", 15 & 36)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7.2 OR (|) operator
#   n1    n2      result
#   1     0        1
#   0     1        1
#   0     0        0
#   1     1        1
print("Binary form of 2 is: ", bin(2))
print("Binary form of 3 is: ", bin(3))
print(" 2 | 3", 2 | 3)
print("Binary form of 15 is: ", bin(15))
print("Binary form of 36 is: ", bin(36))
print(" 15 | 36", 15 | 36)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7.3 XOR (^) Operator
#   n1    n2      result
#   1     0        1
#   0     1        1
#   0     0        0
#   1     1        0
print("Binary form of 2 is: ", bin(2))
print("Binary form of 3 is: ", bin(3))
print(" 2 ^ 3", 2 ^ 3)
print("Binary form of 15 is: ", bin(15))
print("Binary form of 36 is: ", bin(36))
print(" 15 ^ 36", 15 ^ 36)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7.4 NOT (~) Operator
# n   result
# 0    1
# 1    0
print("Binary form of 2 is: ", bin(2))
print("~2", ~2)
print("Binary form of 3 is: ", bin(3))
print("~3", ~3)
print("Binary form of 15 is: ", bin(15))
print("Binary form of 36 is: ", bin(36))
print("~ 15", ~15)
print("~ 36", ~36)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7.5 Left shift operator (<<)
print("Binary form of 6 is: ", bin(6))
print("6 << 2 is: ", 6 << 2)
print("Binary form of 847 is: ", bin(847))
print("847 << 4 is: ", 847 << 4)

# 7.6 Right Shift Operator (>>)
print("Binary form of 6 is: ", bin(6))
print("6 >> 2 is: ", 6 >> 2)
print("Binary form of 847 is: ", bin(847))
print("847 >> 4 is: ", 847 >> 4)






