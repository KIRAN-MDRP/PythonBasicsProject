# This programm illustrates how to validate that given number is Prime Number or Not
inputNumber = int(input("Please enter a number: "))
print("Entered number is: ", inputNumber, " and ", end=" ")
divisorsList = []
for index in range(1,inputNumber+1):
    if inputNumber % index == 0:
        divisorsList.append(index)
if len(divisorsList) == 2 and 1 in divisorsList and inputNumber in divisorsList:
    print("the number is prime")
else:
    print("the number is not prime")
