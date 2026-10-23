# This program demonstrates an inner class.
class Library:
    def __init__(self):
        print("Library class constructor")

    def printLibraryName(self):
        return "Satyanaryana Knowledge"

    class Books:
        def __init__(self):
            print("Books class constructor")
            self.lbr = Library()

        def printBookName(self):
            print("Python book is available at {} Library".format(self.lbr.printLibraryName()))
lbr = Library()
print(lbr.printLibraryName())
bks = lbr.Books()
bks.printBookName()
# bks = Library().Books().printBookName()
