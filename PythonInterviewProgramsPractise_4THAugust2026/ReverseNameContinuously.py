youWantsToEnterName = True
while youWantsToEnterName:
    inputSentence = input("Please enter the sentence:")
    characterCheck = True
    for eachCharacter in inputSentence:
        if ord(eachCharacter) in range(97, 123) or ord(eachCharacter) in range(65, 91) or ord(eachCharacter) == 32 or ord(eachCharacter) == 46:
            characterCheck = True
        else:
            characterCheck = False
            break
    if characterCheck == False:
        print("Entered sentence {} is invalid! Please enter sentence".format(inputSentence))
    else:
        print("Entered sentence {} is valid!".format(inputSentence))
        sentence_1 = inputSentence.split(" ")
        outputSentence = []
        for eachSentence in sentence_1:
            outputSentence.append(eachSentence[::-1])
        outputSentence = " ".join(outputSentence)
        print("Output sentence after each word reversed is: {}".format(outputSentence))
    checkWish = input("Do you wants to enter another sentence again?(yes/no)")
    if checkWish == "yes":
        youWantsToEnterName = True
    else:
        youWantsToEnterName = False
        print("Thank you very much for using this application. Have a great day!")