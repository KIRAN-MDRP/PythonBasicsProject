# Enter name continuously until user wants to stop
iWantToEnterName = True
while iWantToEnterName:
    inputName = input("Enter your name: ")
    print("Your name is {}.".format(inputName))
    checkUserWish = input("Do you want to enter another name? (y/n): ")
    if checkUserWish == "y":
        iWantToEnterName = True
    else:
        iWantToEnterName = False

# Enter name continuously and check entered name is palindrome or not.
wantToCheckPalindrome = True
while wantToCheckPalindrome:
    inputName = input("Please enter name to check palindrome or not:").lower()
    if inputName == inputName[::-1]:
        print("{} is palindrome.".format(inputName))
    else:
        print("{} is not palindrome.".format(inputName))
    checkUserWish = input("Do you want to check another name? (y/n): ")
    if checkUserWish == "y":
        wantToCheckPalindrome = True
    else:
        wantToCheckPalindrome = False

# Enter name continuously and print how many vowels and consonents are there in entered name
wantToGetVowelsAndConsonantsCount = True
vowelsList = ['a', 'e', 'i', 'o', 'u']
vowelsCount = 0
consonantsCount = 0
while wantToGetVowelsAndConsonantsCount:
    inputString = input("Please enter name to get vowels and consonents count:").lower()
    for currentIndex in range(len(inputString)):
        if inputString[currentIndex] in vowelsList:
            vowelsCount += 1
        elif inputString[currentIndex].isalpha():
            consonantsCount += 1
    print("Vowels count: {}, Consonents count: {}".format(vowelsCount, consonantsCount))
    checkUserWish = input("Do you want to check another name? (y/n): ")
    if checkUserWish == "y":
        wantToGetVowelsAndConsonantsCount = True
        vowelsCount = 0
        consonantsCount = 0
    else:
        wantToGetVowelsAndConsonantsCount = False