inputString = input("Please enter the input string: ")
vowelsList = ['a','e','i','o','u','A','E','I','O','U']
vowelsCount = 0
consonantCount = 0
startIndex = 0
while startIndex < len(inputString):
    if inputString[startIndex] in vowelsList:
        vowelsCount += 1
    else:
        if inputString[startIndex].isspace():
            consonantCount += 1
    startIndex += 1
print("There are {} vowels and {} consonants.".format(vowelsCount, consonantCount))