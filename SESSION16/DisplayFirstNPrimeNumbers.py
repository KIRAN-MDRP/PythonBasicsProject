numberInput = int(input("Enter a number: "))
print("First ",numberInput, " Prime Numbers list is:")
numberOne = 2
numbersCounter = 0
primeNumbersCollection = []

while numbersCounter < numberInput:
    IsNumberPrime = True
    for currentNumber in range(2, int(numberOne ** 0.5) + 1):
        if  numberOne % currentNumber== 0:
            IsNumberPrime = False
            break
    if  IsNumberPrime:
         primeNumbersCollection.append(numberOne)
         numbersCounter+=1
    numberOne+=1
print(primeNumbersCollection)