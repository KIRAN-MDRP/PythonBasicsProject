class CheckGivenTwoStringsAreSameAnagramOrNot:
    def checkGivenTwoStringsAreSameAnagramOrNot(self):
        checkString = True
        while checkString:
            inputStr1 = input("Enter the first string: ")
            inputStr2 = input("Enter the second string: ")
            if sorted(inputStr1) == sorted(inputStr2):
                print("The given two strings {} and {} are anagrams!".format(inputStr1, inputStr2))
            else:
                print("The given two strings {} and {} are not anagrams!".format(inputStr1, inputStr2))
            getUserWish = input("Do you want to check again? (y/n): ")
            if getUserWish.lower() != 'y':
                print("Thanks for using this application")
                checkString = False
cgtsasaon = CheckGivenTwoStringsAreSameAnagramOrNot()
cgtsasaon.checkGivenTwoStringsAreSameAnagramOrNot()