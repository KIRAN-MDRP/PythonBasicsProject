getSum = True
while getSum:
    inputNumber = int(input("Please enter number: "))
    firstNumber = 1
    cumulativeSum = 0
    while firstNumber <= inputNumber:
        cumulativeSum += firstNumber
        firstNumber += 1
    print("Sum of first {} numbers is {}.".format(inputNumber, cumulativeSum))
    print("Do you want to continue? (y/n):")
    continueOrNot = input()
    if continueOrNot == "y":
        getSum = True
    else:
        getSum = False