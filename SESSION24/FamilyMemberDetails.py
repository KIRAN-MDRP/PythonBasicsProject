class FamilyMemberDetails:
    """This class represents the details of a family members. If couple having children then couple details along with children details get displayed!"""
    def __init__(self, father, mother, children1, children2, children3):
        """ This constructor initializes the family member details with father, mother, and children details. """
        self.father = father
        self.mother = mother
        self.children1 = children1
        self.children2 = children2
        self.children3 = children3

    # def __init__(self,husband, wife):
    #     """ This method initializes the family member details with husband and wife details. """
    #     self.husband = husband
    #     self.wife = wife

    # def displayFamilyDetails(self):
    #     """ This method displays the family member details. """
    #     print(f"Father name is: {self.father}, Mother name is: {self.mother}, Children names are: {self.children1}, {self.children2}, and , {self.children3}")

    # def coupleDetails(self):
    #     """ This method displays the couple details. """
    #     print(f"Husband name is: {self.husband}, Wife name is: {self.wife}")

fmd1 = FamilyMemberDetails("M.M.SATYANARAYANA", "M.DURGA KUMARI", "M.B.B.KIRAN KUMAR", "M.SATISH KUMAR", "M.SUDHIR KUMAR")
student_Dict = fmd1.__dict__
print(student_Dict)
print(fmd1.__doc__)
print(fmd1.__init__.__doc__)
# fmd1.displayFamilyDetails()

# fmd2 = FamilyMemberDetails("M.M.SATYANARAYANA", "M.DURGA KUMARI")
# fmd1.coupleDetails()