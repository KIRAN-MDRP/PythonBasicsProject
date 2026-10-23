# This program returns repeated character and Non repeated character set from given string
from collections import Counter
class RepeatUniqueCharacterSets:
	def repeatUniqueCharacterSets(self):
		repeatCharacterSet = set()
		uniqueCharacterSet = set()
		inputString = input("Please enter a String to print repeat and Characters String:")
		print(f"Entered String is: {inputString}")
		counter = Counter(inputString)
		for index, character in enumerate(inputString):
			if not character.isspace():
				if counter[character] == 1:
					uniqueCharacterSet.add(character)
				else:
					repeatCharacterSet.add(character)
		return set(list(repeatCharacterSet)), set(list(uniqueCharacterSet))
ruc = RepeatUniqueCharacterSets()
repeat, unique = ruc.repeatUniqueCharacterSets()
print(f"Unique Characters Set is: {unique}")
print(f"Repeated Characters Set is: {repeat}")