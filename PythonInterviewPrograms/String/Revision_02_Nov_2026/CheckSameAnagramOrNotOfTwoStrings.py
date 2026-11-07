class CheckTwoStringsAreSameAnagramOrNot:
	def checkSameAnagram(self):
		wishToCheck = True
		while (wishToCheck):
			finput = input("Please enter the first input:")
			sinput = input("Please enter the second input:")
			print("Entered two strings are: {} and {} respectively!".format(finput, sinput))
			if sorted(finput) == sorted(sinput):
				print("The given two strings are same anagram!")
			else:
				print("The given two strings are not same anagram!")
			userWish = input("Do you wants to check with another set of two strings?(y/n)")
			if userWish == "y":
				wishToCheck = True
			else:
				print("Thans for using this application! Have a great day!")
				wishToCheck = False
ctsasaon = CheckTwoStringsAreSameAnagramOrNot()
ctsasaon.checkSameAnagram()