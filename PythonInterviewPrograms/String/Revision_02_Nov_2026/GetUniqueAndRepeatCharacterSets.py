from collections import Counter


class GetUniqueAndRepeatCharactersSets:
    def getUniqueAndRepeat(self):
        inputData = input("Please enter the input String:")
        print("Entered input data is: {}".format(inputData))
        uniqueSet = set()
        repeatSet = set()
        characterCounter = Counter(inputData)
        for index, element in enumerate(inputData):
            if characterCounter[element] == 1:
                uniqueSet.add(element)
            else:
                repeatSet.add(element)
        return uniqueSet, repeatSet

    def getUserOpinion(self):
        wishTocheck = True
        while (wishTocheck):
            u,r = GetUniqueAndRepeatCharactersSets.getUniqueAndRepeat(self)
            print("Before sorted Unique and Repeat Characters sets are: {} {} respectively!".format(u,r))
            print("After sorted Unique and Repeat Characters sets are: {} {} respectively!".format(sorted(u),sorted(r)))
            wishTocheck = False
            checkUserWish = input("\n Do you wants to check another String?(Y/N)")
            if not checkUserWish == "Y":
                print("Thanks for using this application! Have a great day!")
                wishTocheck = False
            else:
                wishTocheck = True
guarcs = GetUniqueAndRepeatCharactersSets()
guarcs.getUserOpinion()


