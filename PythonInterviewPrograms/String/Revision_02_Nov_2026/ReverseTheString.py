class ReverseString:
	def reverseString(self):
		wishToCheck = True
		while wishToCheck:
			inputString = input("Please enter the input String:")
			print("Entered input String is: {}".format(inputString))
			print("Reversed string is: {}".format(inputString[::-1]))
			checkWish = input("Please let us know do you wants to chack for another string?(y/n)")
			if not checkWish == 'y':
				print("Thanks for using this application!")
				wishToCheck = False
			else:
				wishToCheck = True
rs = ReverseString()
rs.reverseString()