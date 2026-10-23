# In this programm will discuss about different types of functions
# function without parameters and retur type
def wish():
    print("Hello Student Welcome to Python Programming!")

# function with single and multiple parameters and return type.
def displayName(name):
    print("Hello {} welcome to Python Programming!".format(name))

def displayStudentDetails(name, age, course, mobile):
    print("Student name is: {}, age is: {}, course is: {}, mobile is: {}.".format(name, age, course, mobile))

def getParentDetails(studentName):
    return "{} is son of {}".format(studentName, "M.M.Satyanarayana")

def printMultiplicationTable(maxIndex):
    number = int(input("Please enter a number: "))
    for currentNumber in range(1,maxIndex+1):
        print("{} * {} = {}".format(number,currentNumber,number*currentNumber))


# Call the funtions one by one.
wish()
displayName("Mandarapu BalaBalaji KiranKumar")
displayStudentDetails("Satish Kumar",32,"B.Tech",9121530428)
print(getParentDetails("Sudhir Kumar"))
printMultiplicationTable(10)