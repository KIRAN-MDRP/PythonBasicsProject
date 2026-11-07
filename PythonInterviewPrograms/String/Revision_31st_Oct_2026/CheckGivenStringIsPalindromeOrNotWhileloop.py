class CheckPalindromeWhileLoop:
    def checkPalindromeOrNotWhileLoop(self):
        wishToCheck = True
        while wishToCheck:
            inputData = input("Please enter the string:")
            if inputData.isspace() or inputData == "":
                print("Invalid input. Please enter a valid string.")
                continue
            else:
                if inputData == inputData[::-1]:
                    print("The entered string {} is a palindrome.".format(inputData))
                else:
                    print("The entered string {} is not a palindrome.".format(inputData))
                getTheUserWish = input("Do you want to check another string? (yes/no): ").lower()
                if getTheUserWish != "yes":
                    print("Thank you for using the palindrome checker.")
                    wishToCheck = False
cpwl = CheckPalindromeWhileLoop()
cpwl.checkPalindromeOrNotWhileLoop()