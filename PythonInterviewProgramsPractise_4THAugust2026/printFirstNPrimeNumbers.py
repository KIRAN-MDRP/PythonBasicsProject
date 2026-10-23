inputNumber = int(input("Please enter how many number of first Prime numbers you wants to print?"))
print("First {} prime numbers are:".format(inputNumber))
firstPrimeNumber = 2
primeNumbersCounter = 0
while primeNumbersCounter < inputNumber:
	isItPrime = True
	for number in range(2, int(firstPrimeNumber ** 0.5)+1):
		if (firstPrimeNumber % number) == 0:
			isItPrime = False
			break
	if isItPrime:
		print(firstPrimeNumber, end = " ")
		primeNumbersCounter += 1
	firstPrimeNumber += 1
