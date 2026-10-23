inputPrimeNumbers = int(input("Please enter how many prime numbers you wants?"))
firstPrimeNumber = 2
primeNumbersCounter = 0
prineNumbersList = []
while primeNumbersCounter < inputPrimeNumbers:
    isPrimeNumber = True
    for currentNumber in range(2, int(firstPrimeNumber**0.5)+1):
        if firstPrimeNumber % currentNumber == 0:
            isPrimeNumber = False
            break
    if isPrimeNumber:
        prineNumbersList.append(firstPrimeNumber)
        primeNumbersCounter += 1
    firstPrimeNumber += 1
print("List of first ", inputPrimeNumbers, " prime numbers is:",prineNumbersList)
print("And the sum is:", sum(prineNumbersList))
