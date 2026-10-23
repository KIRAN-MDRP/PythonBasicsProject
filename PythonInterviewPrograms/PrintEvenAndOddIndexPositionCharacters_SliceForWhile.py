enterString = input("Enter a string: ")
evenIndexCharactersList = []
oddIndexCharactersList = []
print("Entered string is: {} and length is: {}".format(enterString, len(enterString)))
# print("Using Slice:")
# print("Even index position characters are: {}".format(enterString[0::2]))
# print("Odd index position characters are: {}".format(enterString[1::2]))
# print("+++++++++++++++++++++++++++++++++++++++++++")


# print("Using For loop:")
# for currentIndex in range(len(enterString)):
#     if enterString[currentIndex].isalpha():
#         if currentIndex % 2 == 0:
#             evenIndexCharactersList.append(enterString[currentIndex])
#         else:
#             oddIndexCharactersList.append(enterString[currentIndex])
# print("Even index position characters are: {} and count is: {}".format(evenIndexCharactersList, len(evenIndexCharactersList)))
# print("Odd index position characters are: {} and count is: {}".format(oddIndexCharactersList, len(oddIndexCharactersList)))
# print("+++++++++++++++++++++++++++++++++++++++++++")

print("Using While loop:")
currentIndex = 0
while currentIndex < len(enterString):
    if enterString[currentIndex].isalpha():
        if currentIndex % 2 == 0:
            evenIndexCharactersList.append(enterString[currentIndex])
        else:
            oddIndexCharactersList.append(enterString[currentIndex])
    currentIndex += 1
print("Even index position characters are: {} and count is: {}\n".format(evenIndexCharactersList, len(evenIndexCharactersList)))
print("Odd index position characters are: {} and count is: {}\n".format(oddIndexCharactersList, len(oddIndexCharactersList)))
print("+++++++++++++++++++++++++++++++++++++++++++")

