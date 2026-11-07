class PrintFirstNPrimeNumbers:
    def printFirstNPrimeNumbers(self) -> list():
        inputNumber = int(input("Please enter the number of prime numbers your wants?"))
        print("We are going to print first {} prime numbers")
        firstPrimeNumber = 2
        primeNumbersCounter = 0
        primeNumbersList = []
        while primeNumbersCounter < inputNumber:
            isItPrimeNumber = True
            for number in range(2, int((firstPrimeNumber ** 0.5) + 1)):
                if firstPrimeNumber % number == 0:
                    isItPrimeNumber = False
                    break
            if isItPrimeNumber:
                primeNumbersList.append(firstPrimeNumber)
                primeNumbersCounter += 1
            firstPrimeNumber += 1
        return primeNumbersList


pfnpn = PrintFirstNPrimeNumbers()
print(pfnpn.printFirstNPrimeNumbers())
