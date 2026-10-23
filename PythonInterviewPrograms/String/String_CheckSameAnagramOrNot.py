class CheckOrderOfTwoStrings:
    def compareStrings(self, str1, str2):
        if sorted(str1) == sorted(str2):
            print("The order of characters in both strings is the same.")
        else:
            print("The order of characters in both strings is not the same.")

cpos = CheckOrderOfTwoStrings()
cpos.compareStrings("hello", "olleh")
cpos.compareStrings("hello", "world")