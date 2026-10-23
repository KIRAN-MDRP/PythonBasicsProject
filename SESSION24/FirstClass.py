class MyFirstClass:
    '''This is a class with the name MyFirstClass'''
    '''It simply displays entereed name'''

    def __init__(self,name):
        '''This is default construcctor of the class simply display a message'''
        self.classStudentNamee = name
        print("Hello Learner Welcome to Python")

    def display_name(self):
        '''This method displays the entered name'''
        print("Entered name is:", self.classStudentNamee)

#help(MyFirstClass)
mfc1 = MyFirstClass("KiranKumar")
mfc1.display_name()
mfc2 = MyFirstClass("Balaji")
mfc2.display_name()

