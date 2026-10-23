# This program illustrates about String data Structure.
# Through 5 ways we can create a string.
# First way is by using single quotes.
# Second way is by using double quotes.
# Third way is by using triple quotes.
# Fourth way is by using back quotes.
# Fifth way is by using f-strings.
# Sixth way is by using raw strings
# Seventh way is by using str() constructor.

# Different ways to create a string.
# 1)Using single quotes.
stringUsingSingleQuotes = 'This String is created using single quotes.'
print(stringUsingSingleQuotes)
print(type(stringUsingSingleQuotes))

# 2)Using double quotes.
stringUsingDoubleQuotes = "This String is created using double quotes."
print(stringUsingDoubleQuotes)
print(type(stringUsingDoubleQuotes))

# 3)Using triple quotes.
stringUsingTripleQuotes = """This String is created using triple quotes."""
print(stringUsingTripleQuotes)
print(type(stringUsingTripleQuotes))

# 4)Using back quotes.
stringUsingBackQuotes = '''This String is created using back quotes.'''
print(stringUsingBackQuotes)
print(type(stringUsingBackQuotes))

# 5)Using f-strings.
stringUsingFStrings = f"This String is created using f-strings."
print(stringUsingFStrings)
print(type(stringUsingFStrings))

# 6)Using raw strings.
stringUsingRawStrings = r"This String is created using raw strings."
print(stringUsingRawStrings)
print(type(stringUsingRawStrings))

# 7)Using str() constructor.
stringUsingStrConstructor = str("This String is created using str() constructor.")
print(stringUsingStrConstructor)
print(type(stringUsingStrConstructor))

# String methods
stringOne = "Hello KiranKumar. Welcome to Python Programming Language!"
print("String members and methods are:",dir(stringOne))

# There are 47 methods are there in String.
# 17 methods are left&right methods
# (find,rfind,index,rindex,removeprefix,removesuffix,startswith,endswith,split,rsplit,partition,rpartition,strip,lstrip,rstrip,ljust,rjust)
# # 12 is___ methods
# (isalnum,isalpha,isascii,isdecimal,isdigit,isidentifier,islower,isspace,isnumeric,isprintable,istitle,isupper)
# 18 unique methods
# (capitalize,casefold,center,count,encode,splitlines,expandtabs,format,format_map,zfill,join,swapcase,replace,translate,maketrans,lower,upper,title)
# 01. capitalize  02.casefold   03.center       04.count        05.encode       06.startswith 07.endswith  08.split     09.rsplit    10.splitlines
# 11.expandtabs   12.format     13.format_map   14.index        15.rindex       16.ljust      17.rjust     18.lstrip    19.rstrip    20.strip
# 21.partition    22.rpartition 23.find         24.rfind        25.isalnum      26.isalpha    27.isnumeric 28.isdecimal 29.isdigit   30.isascii
# 31.isidentifier 32.islower    33.isupper      34.isspace      35.isprintable  36.istitle    37.join      38.maketrans 39.translate 40.lower
# 41.upper        42.swapcase   43.title        44.removeprefix 45.removesuffix 46.replace    47.zfill

# 1. capitalize() - Returns a copy of the string with its first character capitalized.
capitalizeStringInput = "this is the captilize string input!"
print("Capitalized String Input:",capitalizeStringInput)
print("capitalizeStringInput.capitalize():",capitalizeStringInput.capitalize())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 2. casefold() - Returns a copy of the string with all the characters converted to lowercase.
casefoldStringInput = "This is the casefold string input!"
print("Casefold String Input:",casefoldStringInput)
print("casefoldStringInput.casefold():",casefoldStringInput.casefold())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 3. center(length to be specified here) - Returns a centered string of length width.
centerStringInput = "Harish Munaga"
print("Center String Input:",centerStringInput)
print("centerStringInput.center(60):",centerStringInput.center(60))
print("centerStringInput.center(60, '*'):",centerStringInput.center(60, '*'))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 4. count() - Returns the number of occurrences of a substring in the string.
countStringInput = "This is the count string input!"
print("Count String Input:",countStringInput)
print("countStringInput.count('is'):",countStringInput.count('is'))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 5. encode() - Returns an encoded version of the string.
encodeStringInput = "This is the encode string input!"
print("Encode String Input:",encodeStringInput)
print("encodeStringInput.encode():",encodeStringInput.encode())
print("encodeStringInput.encode('UTF-8'):",encodeStringInput.encode('UTF-8'))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 6.startswith() - Returns True if the string starts with the specified prefix, otherwise returns False.
startswithStringInput = "This is the startswith string input!"
print("Startswith String Input:",startswithStringInput)
print("startswithStringInput.startswith('This'):",startswithStringInput.startswith('This'))
print("startswithStringInput.startswith('is'):",startswithStringInput.startswith('is'))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 7. endswith() - Returns True if the string ends with the specified suffix, otherwise returns False.
endswithStringInput = "This is the endswith string input!"
print("Endswith String Input:",endswithStringInput)
print("endswithStringInput.endswith('input!'):",endswithStringInput.endswith('input!'))
print("endswithStringInput.endswith('is'):",endswithStringInput.endswith('is'))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 8.split() - Returns a list where the string has been split at each match, starting from the left.
splitStringInput = "This is the split string input!"
print("Split String Input:",splitStringInput)
print("splitStringInput.split():",splitStringInput.split())
print("'Apple','Banana','Cherry','Mango'".split(",",1))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 9.rsplit() - Returns a list where the string has been split at each match, starting from the right.
rsplitStringInput = "This is the rsplit string input!"
print("Rsplit String Input:",rsplitStringInput)
print("rsplitStringInput.rsplit():",rsplitStringInput.rsplit())
print("'Apple','Banana','Cherry','Mango'".rsplit(",",1))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 10.splitlines() - Returns a list where the string has been split at each line break.
splitlinesStringInput = "This is the splitlines string input!\nThis is the second line of the splitlines string input!"
print("Splitlines String Input:",splitlinesStringInput)
print("splitlinesStringInput.splitlines():",splitlinesStringInput.splitlines())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 11. expandtabs() - Returns a copy of the string where all tab characters are replaced by one or more spaces, depending on the current tab size.
expandtabsStringInput = "This\tis\tthe\texpandtabs\tstring\tinput!"
print("Expandtabs String Input:",expandtabsStringInput)
print("expandtabsStringInput.expandtabs():",expandtabsStringInput.expandtabs())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 12.format() - Returns a formatted version of the string.
firstName = "KiranKumar"
middleName = "BalaBalaji"
surName = "Mandarapu"
studentOneDetails = {"Name":"KiranKumar BalaBalaji Mandarapu","Mobile":"9705430428"}
studentTwoDetails = {"Name":"SivaKumar BalaBalaji Mandarapu","Mobile":"9666036339"}
print(f"Student Full Name is: {firstName} {middleName} {surName}")
print("Student Full Name is: {1} {0} {2}".format("SivaKumar","BalaBalaji","Mandarapu"))
print("Student One Name is: {Name} and Contact Number is: {Mobile}".format(**studentOneDetails))
print("Student Two Name is: {Name} and Contact Number is: {Mobile}".format(**studentTwoDetails))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 13.format_map() - Returns a formatted version of the string.
print("Using format_map() method")
print("Student One Name is: {Name} and Contact Number is: {Mobile}".format_map(studentOneDetails))
print("Student Two Name is: {Name} and Contact Number is: {Mobile}".format_map(studentTwoDetails))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# left and right side methods
# 14.index(string to search) - Searches the string for a specified value and returns the position of where it was found from left side.
indexInputString = "python is first complete functional programming language. python is very easy to learn. python is wonderful language"
print("indexInputString is:", indexInputString)
print("indexInputString.index('python')",indexInputString.index("python"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 15.rindex(string to search) - Searches the string for a specified value and returns the position of where it was found from right side.
rindexInputString = "python is first complete functional programming language. python is very easy to learn. python is wonderful language"
print("rindexInputString is: ", rindexInputString)
print("rindexInputString.rindex('python')", rindexInputString.rindex("python"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 16.ljust() - Returns a left justified version of the string
print("'Hello'.ljust(10) is:","Hello".ljust(10))
print("'Hello'.ljust(10,'*')","Hello".ljust(10,"*"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 17.rjust() - Returns a right justified version of the string
print("'Hello'.rjust(10) is:","Hello".rjust(10))
print("'Hello'.rjust(10,'*') is:","Hello".rjust(10,"*"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 18.lstrip() - Returns a left trim version of the string
print("' Hello '.lstrip() is:","Hello".lstrip())
print("'Hello'.lstrip('H') is:","Hello".lstrip("H"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 19.rstrip() - Returns a right trim version of the string
print("' Hello '.rstrip() is:","Hello".rstrip())
print("'Hello'.rstrip('o') is: ","Hello".rstrip("o"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 20.strip() - Returns a trim version of the string
print("' Hello '.strip() is:","Hello".strip())
print("'Hello'.strip('H') is: ","Hello".strip("H"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 21.partition() - Returns a tuple where the string is parted into three parts. Partition starts from left side
# **** Both partition and split returns the tuple and list respectively but the main difference is
# in resultant datastructure(either tuple or list) for the partition matching string also an element means
# resultant datastructure contains matching string where as in case of split matching string excluded.
print("'Python is my favourite programming language'.partition(" ") is:","Python is my favourite programming language".partition(" "))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 22.rpartition() - Returns a tuple where the string is parted into three parts. Partition starts from right side
print("'Python is my favourite programming language'.rpartition(" ")","Python is my favourite programming language".rpartition(" "))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 23. find() - Returns the index of the first occurrence of the specified value, otherwise returns -1 search process will start from left side.
findInputString = "kiran is the java programming language. kiran is good at programming. kiran's aspiration is to become prompt engineer. kiran is working on that."
print("findInputString is: ",findInputString)
print("findInputString.find('kiran') is:",findInputString.find("kiran"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 24.rfind() - Returns the index of the last occurrence of the specified value, otherwise returns -1 search process will start from right side.
rfindInputString = "kiran is the java programming language. kiran is good at programming. kiran's aspiration is to become prompt engineer. kiran is working on that."
print("rfindInputString is: ",rfindInputString)
print("rfindInputString.rfind('kiran') is:",rfindInputString.rfind("kiran"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# is____ methods
# 25.isalnum() - Returns True if all characters in the string are alphanumeric.
alPhaNumericTrue = "SivaKumar23"
alphaNumericFalse = "S1"
print("Is {} only Alpha Numeric: {}?".format(alPhaNumericTrue,alPhaNumericTrue.isalnum()))
print("Is {} only Alpha Numeric: {}?".format(alphaNumericFalse,alphaNumericFalse.isalnum()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 26.isalpha() - Returns True if all characters in the string are in the alphabet
alphaTrue = "SivaKumar"
alphaFalse = "S&"
print("Is {} only Alphabates: {}?".format(alphaTrue,alphaTrue.isalpha()))
print("Is {} only Alphabates: {}?".format(alphaFalse,alphaFalse.isalpha()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 27. isnumeric() - Returns True if all characters in the string are numeric characters where input string contains digits in any format
numericTrue = "12345"
numericFalse = "12345a"
print("Is {} only Numeric: {}?".format(numericTrue,numericTrue.isnumeric()))
print("Is {} only Numeric: {}?".format(numericFalse,numericFalse.isnumeric()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 28.isdecimal() - Returns True if all characters in the string are decimals excluding superscript and subscript characters
decimalTrue = "12345"
decimalFalse = "12345a"
print("Is {} only Decimal: {}?".format(decimalTrue,decimalTrue.isdecimal()))
print("Is {} only Decimal: {}?".format(decimalFalse,decimalFalse.isdecimal()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 29.isdigit() - Returns True if all characters in the string are digits including superscript and subscript characters
digitTrue = "12345"
digitFalse = "12345a"
print("Is {} only Digits: {}?".format(digitTrue,digitTrue.isdigit()))
print("Is {} only Digits: {}?".format(digitFalse,digitFalse.isdigit()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 30.isascii() - Returns True if all characters in the string are ascii characters
asciiTrue = "SivaKumar"
asciiFalse = "~"
print("Is {} only ASCII: {}?".format(asciiTrue,asciiTrue.isascii()))
print("Is {} only ASCII: {}?".format(asciiFalse,asciiFalse.isascii()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 31.isidentifier() - Returns True if the string is a valid identifier
# A valid identifier can contain only letters, numbers, and underscores, but cannot start with a number
identifierTrue = "SivaKumar"
identifierFalse = "12345"
print("Is {} a valid Identifier: {}?".format(identifierTrue,identifierTrue.isidentifier()))
print("Is {} a valid Identifier: {}?".format(identifierFalse,identifierFalse.isidentifier()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 32.islower() - Returns True if all characters in the string are lowercase
lowerTrue = "sivakumar"
lowerFalse = "SivaKumar"
print("Is {} only Lowercase: {}?".format(lowerTrue,lowerTrue.islower()))
print("Is {} only Lowercase: {}?".format(lowerFalse,lowerFalse.islower()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 33.isUpper() - Returns True if all characters in the string are uppercase
upperTrue = "SIVAKUMAR"
upperFalse = "SivaKumar"
print("Is {} only Uppercase: {}?".format(upperTrue,upperTrue.isupper()))
print("Is {} only Uppercase: {}?".format(upperFalse,upperFalse.isupper()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 34.isspace() - Returns True if all characters in the string are whitespaces
spaceTrue = "   "
spaceFalse = "SivaKumar"
print("Is {} only Whitespace: {}?".format(spaceTrue,spaceTrue.isspace()))
print("Is {} only Whitespace: {}?".format(spaceFalse,spaceFalse.isspace()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 35.isprintable() - Returns True if all characters in the string are printable
printableTrue = "SivaKumar"
printableFalse = "SivaKumar\n"
print("Is {} only Printable: {}?".format(printableTrue,printableTrue.isprintable()))
print("Is {} only Printable: {}?".format(printableFalse,printableFalse.isprintable()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 36.istitle() - Returns True if the string follows the rules of a title
titleTrue = "Siva Kumar"
titleFalse = "siva kumar"
print("Is {} a Title: {}?".format(titleTrue,titleTrue.istitle()))
print("Is {} a Title: {}?".format(titleFalse,titleFalse.istitle()))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 37.join() - Returns a string which is all strings concatenated with the given separator
namesList = ["M.M.Satyanarayana","M.DurgaKumari","M.B.B.KiranKumar","M.SatishKumar","M.SudhirKumar"]
print("namesList is: ",namesList)
print("'-'.join(namesList)","-".join(namesList))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 38.maketrans() - Returns a translation table to be used in translations
# 39.translate() - Returns a translated string
translateTable = str.maketrans("Python","Jython")
print("translateTable is: ",translateTable)
print("'I love Python Programming Language'.translate(translateTable)","I love Python Programming Language".translate(translateTable))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 40.lower() - Converts a string into lower case
print("'Hello'.lower() is: ","Hello".lower())
print("'HELLO'.lower()","HELLO".lower())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 41.upper() - Converts a string into upper case
print("'Hello'.upper() is: ","Hello".upper())
print("'hello'.upper()","hello".upper())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 42.swapcase() - Converts lowercase letters to uppercase and uppercase letters to lowercase
print("'Hello'.swapcase() is:","Hello".swapcase())
print("'heLLLOO'.swapcase() is:","heLLLOO".swapcase())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 43.title() - Converts the first character of each word to upper case
print("'hello world'.title() is:","hello world".title())
print("'Hello World'.title() is:","hello world".title())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 44.removeprefix() - Returns a string where the specified prefix string is removed
# ****** Difference betweeen removeprefix() and lstrip() is removeprefix() removes
# exact instance of pattern string matches where as lstrip() removes all the characters from the left side of the string ******
# similarly for removesuffix() and rstrip() as well ***************
print("'Hello'.removeprefix('H') is:","Hello".removeprefix("H"))
print("'Hello'.removeprefix('He') is:","Hello".removeprefix("He"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 45.removesuffix() - Returns a string where the specified suffix string is removed
print("'Hello'.removesuffix('o') is:","Hello".removesuffix("o"))
print("'Hello'.removesuffix('lo') is:","Hello".removesuffix("lo"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 46.replace() - Returns a string where a specified value is replaced with a specified value
print("'Kiran is good practitioner'.replace('Kiran','Kumar')","Kiran is good practitioner".replace("Kiran","Kumar"))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# 47.zfill() - Fills the string with a specified number of 0 values at the beginning
print("'Hello'.zfill(10) is:","Hello".zfill(10))
print("'Hello'.zfill(5) is:","Hello".zfill(5))
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")













