printTable = True
while printTable:
    numberOfTable = int(input("Please enter number: "))
    lastIndex = int(input("Please enter last index: "))
    firstNumber = 1
    while firstNumber <= lastIndex:
        print("{} * {} = {}".format(numberOfTable, firstNumber, numberOfTable*firstNumber))
        firstNumber += 1
    print("+++++++++++++++++++++++++++++++++++++++++++")
    checkWish = input("Do you want to continue? (y/n):")
    if checkWish == "y":
        printTable = True
    else:
        printTable = False
        print("Thank you for using our program!")