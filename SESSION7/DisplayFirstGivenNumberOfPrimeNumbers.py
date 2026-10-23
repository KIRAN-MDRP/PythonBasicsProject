# Write a program that display first given number of prime numbers
# Here input number provided through input
inputNumber = int(input("Enter a number to display prime numbers: "))
count = 0
firstNumber = 2
while count < inputNumber:
    isPrime = True
    for value in range(2,int(firstNumber ** 0.5)+1):
        if firstNumber % value == 0:
            isPrime = False
            break
    if isPrime:
            print(firstNumber)
            count += 1
    firstNumber +=1
