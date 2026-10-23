# This programm illustrates the members and features of a dictionary in Python.
# Dictionary (dict) is an ordered collection of key-value pairs, where each key is unique
# and associated with a corresponding value.
# Dictionaries are mutable, meaning their contents can be modified after creation.
# Means here Key cannot be duplicated or changed. But Value can be changed or repeated.
# Here in dict both key and value can be any data type.

dictOne = {}
print("Empty Dictionary:", dictOne)
print(type(dictOne))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

dictTwo = {"KiranKumar":"SriLakshmi Bhavani"}
print("Dictionary with single item:", dictTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

dictThree = {1:"KiranKumar",None:"Kumar","Kiran":1,True:False,23.45:None,3+4j:"Kalyanai"}
print("Dictionary with multiple items:", dictThree)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Dictionary methods are:", dir(dictOne))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# There are totally 11 methods in dictionary.
# 1)copy()
print("Before copying dictTwo is: ", dictTwo)
dictTwoCopy = dictTwo.copy()
print("After copying dictTwoCopy is: ", dictTwoCopy)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2)get()
print("Value of Key KiranKumar is: ", dictTwo.get("KiranKumar"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3)itmes()
print("All Items of the dictOne are: ", dictOne.items())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4)keys()
print("All Keys of the dictThree are: ", dictThree.keys())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5)values()
print("All Values of the dictThree are: ", dictThree.values())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6)pop()
# **** Difference between pop() and popitem() is:
# pop(Key) removes item based on key where as popitem() removes the last inserted item from the dictionary.
# *****
print("Before poping dictTwo is: ", dictTwo)
dictTwo.pop("KiranKumar")
print("After poping dictTwo is: ", dictTwo)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7)popitem()
print("Before poping dictThree is: ", dictThree)
dictThree.popitem()
print("After poping dictThree is: ", dictThree)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 8)update()
print("dictThree before update item which is having key Kiran", dictThree)
dictThree.update({"Kiran": 36})
print("After update dictThree is: ", dictThree)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 9)clear()
print("dictThree before clear is: ", dictThree)
dictThreeCopy = dictThree.copy()
dictThree.clear()
print("After clear dictThree is: ", dictThree)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 10)setdefault()
print("dictThree before setdefault item which is not having key Kiran", dictThree)
valueOfKiran = dictThree.setdefault("Kiran", 75)
print("After setdefault dictThree is: ", dictThree)
print("Value of Kiran is: ", valueOfKiran)

print("dictThreeCopy before setdefault item which is having key Kiran", dictThreeCopy)
valueOfKiran = dictThreeCopy.setdefault("Kiran", 75)
print("After setdefault dictThreeCopy is: ", dictThreeCopy)
print("Value of Kiran is: ", valueOfKiran)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 11)fromkeys()
dictFour = dict.fromkeys(["SivaKumar", "KiranKumar", "SatishKumar","SudhirKumar"])
print("New Dictionary created with no value mentioned: ", dictFour)
dictFive = dict.fromkeys(["SivaKumar","KiranKumar","SatishKumar","SudhirKumar"],"Mandarapu")
print("New Dictionary created with value mentioned: ", dictFive)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# I have one list of Names. I needs to get the Names first letter as Key and
# Values are as list of names which are having Key as first character in those Names.
inputList = ["SivaKumar","KiranKumar","SatishKumar","SudhirKumar","sivakumar","kirankumar","satishkumar","sudhirkumar"]
outputDictionaryStartingLetters = {}
outputDictionaryEndsLetter = {}
for name in inputList :
    outputDictionaryStartingLetters.setdefault(name[0],[]).append(name)
    outputDictionaryEndsLetter.setdefault(name[-1],[]).append(name)
print(outputDictionaryStartingLetters)
print(outputDictionaryEndsLetter)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

dictSix = {key:[] for key in ["A","B","C"]}
#dictSix = dict.fromkeys(["A","B","C"])
dictSix["A"].append(1)
print("New Dictionary created with value mentioned: ", dictSix)
print(dictSix["A"] is dictSix["B"])
#dictSix = dict.fromkeys(key:[] for key in ["A","B","C"])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")




