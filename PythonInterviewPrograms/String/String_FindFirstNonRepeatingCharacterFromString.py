from collections import Counter
class FindFirstNonRepeatingCharacter:
    # Traditional approach
    def findFirstNonRepeatingCharacter(self, inputString):
        nonRepeatCharacterList = []
        allCharactersList = list(inputString)
        for character in allCharactersList:
            if allCharactersList.count(character) == 1:
                nonRepeatCharacterList.append(character)
        print(f"First Non repeating character from given string {inputString} is: {nonRepeatCharacterList[0]}")

     # Through enumerate()
    def findFirstNonRepeatingCharacterUsingEnumerate(self, inputString) -> int:
        counter = Counter(inputString)
        for index, character in enumerate(inputString):
            if counter[character] == 1:
                return character
        return -1

ffnrc = FindFirstNonRepeatingCharacter()
ffnrc.findFirstNonRepeatingCharacter("hello")
ffnrc.findFirstNonRepeatingCharacter("KiranKumar")
print(ffnrc.findFirstNonRepeatingCharacterUsingEnumerate("hello"))
print(ffnrc.findFirstNonRepeatingCharacterUsingEnumerate("KiranKumar"))
print(ffnrc.findFirstNonRepeatingCharacterUsingEnumerate("KiranKiran"))