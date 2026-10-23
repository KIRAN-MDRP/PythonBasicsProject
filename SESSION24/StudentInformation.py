class StudentInformation:
    '''This class is used to store student information'''
    def __init__(self,sname,sage,sgender,scontact,saddress):
        self.studentname = sname
        self.studentage = sage
        self.studentgender = sgender
        self.studentcontact = scontact
        self.studentaddress = saddress

    # def show_Student_Information(self):
        # This is one way to display student information
        # print("Entered Student Information is:")
        # print("Name:",self.studentname)
        # print("Age:",self.studentage)
        # print("Gender:",self.studentgender)
        # print("Contact:",self.studentcontact)
        # print("Address:",self.studentaddress)

        # This is second way of display student information
        # print("Student name is: {}, age is: {}, gender is: {}, contact is: {}, address is: {}"
        #       .format(self.studentname,self.studentage,self.studentgender,self.studentcontact,self.studentaddress))

        # This is the third way to display student information
        # print("Student name is: {2}, age is: {3}, gender is: {4}, contact is: {1}, address is: {0}"
        #       .format(self.studentaddress,self.studentcontact,self.studentname,self.studentage,self.studentgender))

        # This is the fourth way to display student information
        # print(f"Student name is: {self.studentname}, age is: {self.studentage}, gender is: {self.studentgender}, contact is: {self.studentcontact}, address is: {self.studentaddress}")
si1 = StudentInformation("KiranKumar",25,"Male",9848022222,"Hyderabad")
# si1.show_Student_Information()
# print(si1.__dict__)
help(si1)