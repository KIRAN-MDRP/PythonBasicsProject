class PrintEitherOnlyCharactersOrLetters:
    def processString(self):
        inputData = input("Please enter a string: ")
        print("Entered string is: {}".format(inputData))
        onlyCharacters = "".join([char for char in inputData if char.isalpha()])
        print("Only characters in the string are: {}".format(onlyCharacters))
        onlyNumbers = "".join([char for char in inputData if char.isdigit()])
        print("Only numbers in the string are: {}".format(onlyNumbers))
peocol = PrintEitherOnlyCharactersOrLetters()
peocol.processString()