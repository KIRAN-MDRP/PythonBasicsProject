# This program demonstrates the use of garbage collector
import time
class GarbageCollectorDemo:
    def __init__(self):
        print("From constructor")

    def __del__(self):
        print("From destructor")

gc = GarbageCollectorDemo()
time.sleep(10)
print("This is the end of the program")
time.sleep(5)