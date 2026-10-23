stringInput = input("Please enter a String:")
print("Entered string is: {} and length is: {}".format(stringInput, len(stringInput)))
loweCase = ""
upperCase = ""
for character in stringInput:
    if character.isalpha():
        if character.isupper():
            upperCase += character
        elif character.islower():
            loweCase += character

print("Lower case characters are: {} and count is: {}".format(loweCase, len(loweCase)))
print("Upper case characters are: {} and count is: {}".format(upperCase, len(upperCase)))