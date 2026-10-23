lengthOfList = int(input("Please enter the length of the list: "))
outputList = []
print("We are going to enter {} number of elements from user input".format(lengthOfList))
counter = 0
while counter < lengthOfList:
    inputData = input("Please enter the element at {} index:".format(counter+1))
    if not inputData.isspace():
        outputList.append(inputData)
    counter += 1
print("Output list is: {}".format(outputList))