class PrintCharacterAndNumbersSeparately:
	def printOnlyNumberAndCharacters(self):
		inputString = input("Please enter the input String:")
		print("Input String is: {}".format(inputString))
		onlyCharacters = "".join(element for element in inputString if element.isalpha())
		onlyNumbers = "".join(element for element in inputString if element.isdigit())
		print("Only Characters is: {}".format(onlyCharacters))
		print("Only Numbers is: {}".format(onlyNumbers))
pcans = PrintCharacterAndNumbersSeparately()
pcans.printOnlyNumberAndCharacters()