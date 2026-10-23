class ReverseString:
    def reverseString(self, inputString):
        print(f"Input String is: {inputString}")
        print(f"Reversed String is: {inputString[::-1]}")
Reverser = ReverseString()
Reverser.reverseString("hello")