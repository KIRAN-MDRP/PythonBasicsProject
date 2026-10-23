inputString = input("Please enter the string:")
uniqueCharactersList = []
repeatedCharactersList = []

for character in inputString:
    if not character.isspace():
        if inputString.count(character) > 1:
            repeatedCharactersList.append(character)
        else:
            uniqueCharactersList.append(character)
print(uniqueCharactersList)
print(list(set(repeatedCharactersList)))
