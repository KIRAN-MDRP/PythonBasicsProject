inputNumber = int(input("Enter how many first n numbers sum do you required?: "))
cumulativeSum = 0
for number in range(0,inputNumber+1,2):
    cumulativeSum += number
print("Cumulative sum of first {} even numbers is {}.".format(inputNumber,cumulativeSum))