class GetLongNonRepeatString:
    def getStringOutput(self):
        wishToCheck = True
        while wishToCheck:
            inputData = input("Please enter the input String:")
            print("Entered input data is: {}".format(inputData))
            left = 0
            maxLength = 0
            outputString = ""
            characterSet = set()
            for right in range(len(inputData)):
                if inputData[right] in characterSet:
                    characterSet.remove(inputData[left])
                    left += 1
                characterSet.add(inputData[right])
                if right - left + 1 > maxLength:
                    maxLength = right - left + 1
                    outputString = inputData[left : right  + 1]
            print("The longest Non repeat SubString is: {}".format(outputString))
            doYouWantsToCheckForAnotherString = input("Do you wants to check for other string?(Yes/No)")
            if doYouWantsToCheckForAnotherString.lower() == "yes":
                wishToCheck = True
            else:
                print("Thanks for using this application! Have a great day!")
                wishToCheck = False
glnrs = GetLongNonRepeatString()
glnrs.getStringOutput()