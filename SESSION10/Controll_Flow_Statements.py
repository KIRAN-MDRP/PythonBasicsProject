# This program illustrates the use of control flow statements in Python
# We have three categories of control flow statements in Python:
# Those are: conditional statements, loop statements, and jump or transfer statements.

# Conditional Statements:
# 1)if
# 2)if else
# 3)nested if else
# 4)elif

# if:
evenInput = int(input("Enter input for even number evaluation: "))
if evenInput % 2 == 0:
    print("Entered number is {} even number.".format(evenInput))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# draw back of if statement: if statement does not have any else block.
# It means if the condition is not true, then it will not execute any code.
# And if we have multiple condidions, it evaluates all the condition even if one of them is true.
ifdrawbackInput = int(input("Please enter any number in the range of 5: "))
if ifdrawbackInput == 1:
    print("Entered number is one.")
if ifdrawbackInput == 2:
    print("Entered number is two.")
if ifdrawbackInput == 3:
    print("Entered number is three.")
if ifdrawbackInput == 4:
    print("Entered number is four.")
if ifdrawbackInput == 5:
    print("Entered number is five.")
else:
    print("Entered number is not in the range of 5.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# if else:
evenoddInput = int(input("Enter a number for even or odd evaluation: "))
if evenoddInput % 2 == 0:
    print("Entered number is {} and it is an even number.".format(evenoddInput))
else:
    print("Entered number is {} and it is a odd number.".format(evenoddInput))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# nested if else: first example (Comparision between two numbers)
firstInput = int(input("Enter first number: "))
secondInput = int(input("Enter second number: "))
if firstInput > secondInput:
    print("{} is greater than {}.".format(firstInput, secondInput))
else:
    if firstInput < secondInput:
        print("{} is less than {}.".format(firstInput, secondInput))
    else:
        print("{} is equal to {}.".format(firstInput, secondInput))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# nested if else: second example (Comparision between three numbers)
first = int(input("Please enter first number:"))
second = int(input("Please enter second number:"))
third = int(input("Please enter third number:"))
if first > second and first > third:
    print("{} is greater than {} and {}.".format(first, second, third))
else:
    if second > first and second > third:
        print("{} is greater than {} and {}".format(second,first,third))
    else:
        if third > first and third > second:
            print("{} is greater than {} and {}".format(third,first,second))
        else:
            print("Numbers {},{} and {} are equal.".format(first,second,third))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# nested if else: with elif
first = int(input("Please enter first number:"))
second = int(input("Please enter second number:"))
third = int(input("Please enter third number:"))
if first > second and first > third:
    print("{} is greater than {} and {}.".format(first, second, third))
elif second > first and second > third:
    print("{} is greater than {} and {}".format(second,first,third))
elif third > first and third > second:
    print("{} is greater than {} and {}".format(third,first,second))
else:
    print("Numbers {},{} and {} are equal.".format(first,second,third))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

## Loop Statements
# In loop statements, we use the 'for' and 'while' keywords to create loops.
# These loops allow us to execute a block of code repeatedly until a certain condition is met.
l1 = [None, 1, 2.34, 3+4J, True]
for element in l1:
    print("{} is {} data type.".format(element,type(element)))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# jump statements
# In jump statements, we use the 'break', 'continue' and 'pass' keywords to control the flow of the program.
# break is used to exit the loop.
# continue is used to skip the current execution and continue with next immediate iteration
# pass is used to do nothing or used to create an empty block of code.
l2 = range(10)
print("Break example:")
for number in l2:
    if number == 5:
        print("Current iteration reached to 5. Thats why exit the loop.")
        break
    print("Break example Current Iteration is {}.".format(number))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Continue example:")
print("Please ignore iterations of even and multiples of 3.")
for number in range(10):
    if number % 2 == 0 or number % 3 == 0:
        continue
    print("Continue example Current Iteration is {}.".format(number))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Pass example:")
for number in range(10):
    if number < 5:
        pass
    else:
        print("Pass example Current Iteration is {}.".format(number))


