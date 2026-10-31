from collections import Counter
class RepeatAndUniqueCharactersFromString:
    def repeatAndUniqueCharactersSet(self):
        inputString = input("Please enter the input String: ")
        print("Entered String is: {}".format(inputString))

        uniqueCharacterSet = set()
        repeatCharacterSet = set()

        characterCounter = Counter(inputString)

        for index, eachCharacter in enumerate(inputString):
            if not eachCharacter.isspace():
                if characterCounter[eachCharacter] == 1:
                    uniqueCharacterSet.add(eachCharacter)
                else:
                    repeatCharacterSet.add(eachCharacter)

        return uniqueCharacterSet, repeatCharacterSet


raucfs = RepeatAndUniqueCharactersFromString()
unique, repeat = raucfs.repeatAndUniqueCharactersSet()
print(
    "Unique characters: {} and Repeated characters: {} respectively!".format(
        sorted(unique), sorted(repeat)
    )
)

