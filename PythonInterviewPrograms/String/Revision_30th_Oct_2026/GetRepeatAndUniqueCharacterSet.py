from collections import Counter
class GetRepeatAndUniqueCharacterSet:
	def getRepeatAndUnique(self):
		inputData = input("Please enter the input String:")
		print("Entered inputData is: {}".format(inputData))
		repeat = set()
		unique = set()
		characterCounter = Counter(inputData)
		for index, element in enumerate(inputData):
			if not element.isspace():
				if characterCounter[element] == 1:
					unique.add(element)
				else:
					repeat.add(element)
		return sorted(repeat), sorted(unique)
grau = GetRepeatAndUniqueCharacterSet()
(r,u) = grau.getRepeatAndUnique()
print("Repeat Character Set is: {}".format(r))
print("Unique Character Set is: {}".format(u))