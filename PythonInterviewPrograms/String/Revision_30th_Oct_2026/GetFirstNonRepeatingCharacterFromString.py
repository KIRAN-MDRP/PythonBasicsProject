from collections import Counter
class GetFirstNonRepeatingCharacterFromString:
    def getFirstNonRepeatingCharacterFromString(self) -> str | int:
        inputString = input("Enter the string: ")
        charCounter = Counter(inputString)
        for index, char in enumerate(inputString):
            if charCounter[char] == 1:
               return char
        return -1
    def whileLoopExec(self):
        wishToCheck = True
        while wishToCheck:
            outputChar = GetFirstNonRepeatingCharacterFromString.getFirstNonRepeatingCharacterFromString(self)
            print("The first non-repeating character is:", outputChar)
            getUserWish = input("Do you want to check again? (y/n): ")
            if getUserWish.lower() != 'y':
                print("Thanks for using this application!")
                wishToCheck = False
gfnrcfs = GetFirstNonRepeatingCharacterFromString()
gfnrcfs.whileLoopExec()

