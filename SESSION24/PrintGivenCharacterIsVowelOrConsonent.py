inputCharacter = input("Enter a character: ")
vowelsList = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
if inputCharacter in vowelsList:
    print("The entered character {} is a vowel.".format(inputCharacter))
else:
    print("The entered character {} is a consonant.".format(inputCharacter))