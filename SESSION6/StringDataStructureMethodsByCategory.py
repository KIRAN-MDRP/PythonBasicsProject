class StringDataStructureMethods:
    def uniqueMethods(self):
        print("capitalize()", end=" ")
        print("casefold()", end=" ")
        print("center()", end = " ")
        print("count()", end = " ")
        print("expandtabs()", end=" ")
        print("encode()", end = " ")
        print("splitlines()", end=" ")
        print("swapcase()", end=" ")
        print("replace()", end=" ")
        print("zfill()", end=" ")
        print("join()", end=" ")
        print("lower()", end=" ")
        print("upper()", end=" ")
        print("title()", end=" ")
        print("format()", end=" ")
        print("format_map()", end=" ")
        print("maketrans()", end=" ")
        print("translate()", end=" ")

    def leftRightMethods(self):
        print("find()", end=" ")
        print("rfind()", end=" ")
        print("index()", end=" ")
        print("rindex()", end=" ")
        print("split()", end=" ")
        print("rsplit()", end=" ")
        print("strip()", end=" ")
        print("lstrip()", end=" ")
        print("rstrip()", end=" ")
        print("ljust()", end=" ")
        print("rjust()", end=" ")
        print("partition()", end=" ")
        print("rpartition()", end=" ")
        print("startswith()", end=" ")
        print("endswith()", end=" ")
        print("removeprefix()", end=" ")
        print("removesuffix()", end=" ")

    def isMethods(self):
        print("isalnum()", end=" ")
        print("isalpha()", end=" ")
        print("isnumeric()", end=" ")
        print("isdigit()", end=" ")
        print("isdecimal()", end=" ")
        print("islower()", end=" ")
        print("isupper()", end=" ")
        print("istitle()", end=" ")
        print("isascii()", end=" ")
        print("isspace()", end=" ")
        print("isprintable()", end=" ")
        print("isidentifier()", end=" ")


    def menu(self):
        userWish = True
        while (userWish):
            print("Please select one number from given menu:")
            print("1)UniqueMethods \n2)LeftRightMethods \n3)IsMethods")
            inputString = int(input("Please select one option from above menu:"))
            if inputString == 1:
                StringDataStructureMethods.uniqueMethods(self)
            elif inputString == 2:
                StringDataStructureMethods.leftRightMethods(self)
            elif inputString == 3:
                StringDataStructureMethods.isMethods(self)
            else:
                print("Please enter valid input.")
                userWish = True
            checkWish = input("Do you wants to get another set of methods?(y/n)")
            if not checkWish == "y":
                print("Thanks for using this application! Have a great day!")
                userWish = False
            else:
                userWish = True


sdsms = StringDataStructureMethods()
sdsms.menu()


