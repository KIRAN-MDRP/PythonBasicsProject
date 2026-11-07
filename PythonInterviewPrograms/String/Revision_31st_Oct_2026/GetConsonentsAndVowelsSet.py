class GetConsonentsAndVowelsSet:
    def getConsonentsAndVowelsSet(self):
        vowelsList = ['a', 'e', 'i', 'o', 'u']
        inputString = input("Please enter the string:")
        vowelsSet = set()
        consonentsSet = set()
        for char in inputString:
            if not char.isspace():
                if char.lower() in vowelsList:
                    vowelsSet.add(char)
                else:
                    consonentsSet.add(char)
        return sorted(vowelsSet), sorted(consonentsSet)
gcavs = GetConsonentsAndVowelsSet()
v,c = gcavs.getConsonentsAndVowelsSet()
print("Vowels in the string:", v)
print("Consonents in the string:", c)