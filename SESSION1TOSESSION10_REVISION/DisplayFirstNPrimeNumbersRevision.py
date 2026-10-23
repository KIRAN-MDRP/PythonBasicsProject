inputNumber = int(input("Please enter the number:"))
primeNoCounter = 0
firstPrimeNumber = 2
primeNumbersList = []
while primeNoCounter < inputNumber:
	isPrime = True
	for ele in range(2, int(firstPrimeNumber ** 0.5)+1):
		if firstPrimeNumber % ele == 0:
			isPrime = False
			break
	if isPrime:
		primeNumbersList.append(firstPrimeNumber)
		primeNoCounter += 1
	firstPrimeNumber += 1
print(primeNumbersList)