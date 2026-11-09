from collections import Counter


class GetFirstUniqueCharacter:
    def getFirstUniqueCharacter(self):
        wish = True
        while wish:
            inputData = input("Please enter the input data:")
            print("Entered input data is: {}".format(inputData))
            self.output = GetFirstUniqueCharacter.getElement(self,inputData)
            if not self.output == -1:
                print(self.output)
            else:
                print("There is not unique character in the given string!")
            userWish = input("Do you wants to check with another string?(y/n)")
            if not userWish == 'y':
                print("Thanks for using this application! Have a great day!")
                wish = False
            else:
                wish = True
    def getElement(self,inputData):
        characterCounter = Counter(inputData)
        for index, element in enumerate(inputData):
            if characterCounter[element] == 1:
                return element
        return -1


gfuc = GetFirstUniqueCharacter()
gfuc.getFirstUniqueCharacter()