# This programm illustrates the concept of list and tuple creation at runtime

listInput = []
listLength = int(input("Please enter the length of the list: "))

print("Entered list length is: ", listLength)
for listIndex in range(listLength):
    print(listIndex)
    listElement = input("Please enter the element for list ")
    listInput.append(listElement)
print("Entered list is: ", listInput)


