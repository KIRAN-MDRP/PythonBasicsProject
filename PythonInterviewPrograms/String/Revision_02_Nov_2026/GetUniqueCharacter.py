from collections import Counter
class GetFirstUniqueCharacter:
    def getFirstUniqueCharacter(self):
        inputString = input("Please enter the input String: ")
        print("Entered input string is: {}".format(inputString))

        characterCounter = Counter(inputString)

        for index, element in enumerate(inputString):
            if characterCounter[element] == 1:
                return element

        return -1


gfuc = GetFirstUniqueCharacter()
output = gfuc.getFirstUniqueCharacter()

if output != -1:
    print("Unique character from the above string is: {}".format(output))
else:
    print("There is no unique character in the above string!")
