# Print first n prime numbers
inputNumber = int(input("Enter a number: "))
firstNumber = 2
count = 0
primeNumbersList = []
while count < inputNumber:
    isPrime = True
    for i in range(2,int(firstNumber ** 0.5) + 1):
        if firstNumber % i == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbersList.append(firstNumber)
        count += 1
    firstNumber +=1
print(primeNumbersList)