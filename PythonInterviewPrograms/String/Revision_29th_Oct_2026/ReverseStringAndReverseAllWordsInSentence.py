class ReverseGivenString:
   def reverseAllWords(self):
        inputSentense = input("Please enter the string:")
        print("Input is: {}".format(inputSentense))
        self.outputList = []
        for eachWord in inputSentense.split(" "):
            self.outputList.append(eachWord[::-1])
        return " ".join(self.outputList)

rgs = ReverseGivenString()
print(rgs.reverseAllWords())
