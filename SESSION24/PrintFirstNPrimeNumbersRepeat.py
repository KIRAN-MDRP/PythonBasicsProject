nPrimeNumbers = int(input("Enter the number of prime numbers to print: "))
firstPrimeNumber = 2
primeNumbersCounter = 0
primeNumbers = []
while primeNumbersCounter < nPrimeNumbers:
    isPrime = True
    for i in range(2, int((firstPrimeNumber**0.5)+1)):
        if firstPrimeNumber % i == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(firstPrimeNumber)
        primeNumbersCounter += 1
    firstPrimeNumber += 1
print(primeNumbers)