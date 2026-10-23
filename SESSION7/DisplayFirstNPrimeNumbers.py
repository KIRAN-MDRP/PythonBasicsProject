numberN = int(input("Please enter the nuumber of first prime numbers:"))
print("We are going to display first ", numberN, " prime numbers.")
counter = 0
firstPrimeNumber = 2
primeNumbersList = []
while counter < numberN:
    isItPrimeNumber = True
    for pn in range(2, int(firstPrimeNumber ** 0.5)+1):
        if firstPrimeNumber % pn == 0:
            isItPrimeNumber = False
            break
    if isItPrimeNumber:
        primeNumbersList.append(firstPrimeNumber)
        counter += 1
    firstPrimeNumber += 1
print(primeNumbersList)
