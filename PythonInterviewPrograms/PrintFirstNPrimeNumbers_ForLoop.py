# This program accepts number of prime numbers to be printed as input and prints the first n prime numbers
from operator import truediv

# noOfPrimeNumbers = int(input("Enter the number of prime numbers to be printed: "))
# firstPrimeNumber = 2
# primeNumbersCounter = 0
# prineNumbersList = []
#
# while primeNumbersCounter < noOfPrimeNumbers:
#     isPrimeNumber = True
#     for n in range(2, int((firstPrimeNumber ** 0.5)+1)):
#         if firstPrimeNumber % n == 0:
#             isPrimeNumber = False
#             break
#     if isPrimeNumber:
#         prineNumbersList.append(firstPrimeNumber)
#         primeNumbersCounter += 1
#     firstPrimeNumber+=1
# print(f"First {noOfPrimeNumbers} prine Numbers list is: {prineNumbersList}")


inputNumber = int(input("Please enter how many prime numbers you wants:"))
firstPrimeNumber = 2
primeNumbersList = []
primeNumbersCounter = 0
while primeNumbersCounter < inputNumber:
	isPrime = True
	for number in range(2, int((firstPrimeNumber ** 0.5)+1)):
		if firstPrimeNumber % number == 0:
			isPrime = False
			break
	if isPrime:
		primeNumbersList.append(firstPrimeNumber)
		primeNumbersCounter += 1
	firstPrimeNumber += 1
print(primeNumbersList)