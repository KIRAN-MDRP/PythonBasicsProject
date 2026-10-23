import os
class ExceptionDemoWithDefaultExceptBlocks:
    def method(self):
        try:
            firstNumber = int(input("Please enter a first number: "))
            os._exit(0)
            raise Exception("This is a custom exception")
            secondNumber = int(input("Please enter a second number: "))
            print("The division of the two numbers is: ", firstNumber / secondNumber)
        except (ZeroDivisionError, ValueError) as message:
            print("An error occurred: ", message)
        except Exception as ec:
            print("An unexpected error occurred: ", ec)
edwde = ExceptionDemoWithDefaultExceptBlocks()
edwde.method()