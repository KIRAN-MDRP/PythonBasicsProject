class CheckPalindromeOrNot:
    def checkString(self, inputString):
        if inputString == inputString[::-1]:
            print("The string {} is a palindrome.".format(inputString))
        else:
            print("The string {} is not a palindrome.".format(inputString))

cpon = CheckPalindromeOrNot()
cpon.checkString("racecar")
cpon.checkString("hello")
