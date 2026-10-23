inputNumber = int(input("Enter which number table you wants to print? "))
lastIndex = int(input("Enter last index of table you wants to print? "))
for index in range(1,lastIndex+1):
    print("{} * {} = {}".format(inputNumber,index,inputNumber*index))