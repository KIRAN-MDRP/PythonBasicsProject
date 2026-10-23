inputString = input("Please enter the string:")
uniqueCharacters = ""
repeatedCharacter= ""

for character in inputString:
    if not character.isspace():
        if inputString.count(character) > 1:
            repeatedCharacters = repeatedCharacter + character
        else:
            uniqueCharacters = uniqueCharacters + character
print(uniqueCharacters)
print(repeatedCharacters)
