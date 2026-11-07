class GetCharacterSymbolNumberSetFromString:
    def getCharactersSymbollsNumbers(self):
        inputData = input("Enter a string: ")
        print("Given input String is: {}".format(inputData))
        charSet = set()
        symSet = set()
        numSet = set()
        for eachCharacter in inputData:
            if eachCharacter.isalpha() and (
                    ord(eachCharacter) in range(65, 91) or ord(eachCharacter) in range(97, 123)):
                charSet.add(eachCharacter)
            elif eachCharacter.isdigit():
                numSet.add(eachCharacter)
            else:
                symSet.add(eachCharacter)
        return sorted(charSet), sorted(symSet), sorted(numSet)

gcsnsfs = GetCharacterSymbolNumberSetFromString()
c,s,n = gcsnsfs.getCharactersSymbollsNumbers()
print("Character set is: {}, Symbol set is: {}, Number set is: {}".format(c,s,n))