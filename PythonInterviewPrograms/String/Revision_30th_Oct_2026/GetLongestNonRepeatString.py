class LongestNonRepeatSubString:
    def getLongestNonRepeatSubString(self):
        wishToCheck = True
        while wishToCheck:
            inputString = input("Please enter the input String: ")
            print("Entered input String is: {}".format(inputString))
            charSet = set()
            longestNonRepeatSubString = ""
            maxLength = 0
            leftIndex = 0
            for right in range(len(inputString)):
                while inputString[right] in charSet:
                    charSet.remove(inputString[leftIndex])
                    leftIndex += 1
                charSet.add(inputString[right])
                if right - leftIndex + 1 > maxLength:
                    maxLength = right - leftIndex + 1
                    longestNonRepeatSubString = inputString[leftIndex:right + 1]
            print("Longest Non Repeated Substring from given String is: {}".format(
                longestNonRepeatSubString))
            print("Length of Longest Non Repeated Substring is: {}".format(maxLength))
            checkWish = input("Do you want to check another string? (Y/N): ")
            if checkWish.lower() == "y":
                wishToCheck = True
            else:
                print("Thanks for using this application!")
                wishToCheck = False
lnrss = LongestNonRepeatSubString()
lnrss.getLongestNonRepeatSubString()

