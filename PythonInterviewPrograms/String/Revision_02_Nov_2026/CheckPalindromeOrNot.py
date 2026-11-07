class PalindromeOrNot:
    def checkPalindrome(self):
        wishToCheck = True
        while wishToCheck:
            inputData = input("Please enter the string:")
            print("Entered String is: {}".format(inputData))
            if inputData == inputData[::-1]:
                print("And it is palindrome")
            else:
                print("And it is not palindrome")
            userWish = input("Do you wants to check with another String?(y/n)")
            if not userWish == "y":
                wishToCheck = False
            else:
                print("Thanks for using this application! Have a great day!")
                wishToCheck = True


pon = PalindromeOrNot()
pon.checkPalindrome()
