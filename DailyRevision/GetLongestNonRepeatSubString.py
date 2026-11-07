class GetLongestNonRepeatSubString:
	def getLongestNonRepeatSubString(self):
		wishToContinue = True
		while wishToContinue:
			inputData = input("Please enter the input String:")
			print("Entered input string is: {}".format(inputData))
			left = 0
			maxLength = 0
			outputString = ""
			characterSet = set()
			for right in range(len(inputData)):
				while inputData[right] in characterSet:
					characterSet.remove(inputData[left])
					left += 1
				characterSet.add(inputData[right])
				if right - left + 1 > maxLength:
					maxLength = right - left + 1
					outputString = inputData[left : right + 1]
			print("The Longest Non Repeat Character from above string is: {}".format(outputString))
			userWish = input("Do you wants to check with another string?(y/n)")
			if not userWish == "y":
				print("Thanks for using this application! Have a great day!")
				wishToContinue = False
			else:
				wishToContinue = True
glnrss = GetLongestNonRepeatSubString()
glnrss.getLongestNonRepeatSubString()