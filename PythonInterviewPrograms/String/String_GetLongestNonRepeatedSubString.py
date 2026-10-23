class String_GetLongestNonRepeatedSubString:
    def getLongestNonRepeatedSubString(self, inputString):
        charSet = set()
        longestNonRepeatedSubString = ""
        left = 0
        maxLength = 0

        for right in range(len(inputString)):
            while inputString[right] in charSet:
                charSet.remove(inputString[left])
                left += 1
            charSet.add(inputString[right])
            if right - left + 1 > maxLength:
                maxLength = right - left + 1
                longestNonRepeatedSubString = inputString[left:right+1]
        return longestNonRepeatedSubString

sglnrs = String_GetLongestNonRepeatedSubString()
s = sglnrs.getLongestNonRepeatedSubString("abcabcbb")
print(s)


