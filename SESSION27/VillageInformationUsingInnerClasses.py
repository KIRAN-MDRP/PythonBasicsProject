class Country:
    def __init__(self):
        pass
    def setCountry(self):
        self.countryName = input("Please enter the country name:")

    def getCountry(self):
        return self.countryName

    class State:
        def __init__(self):
            pass

        def setState(self):
            self.stateName = input("Please enter the state name:")

        def getState(self):
            return self.stateName

        class District:
            def __init__(self):
                pass

            def setDistrictName(self):
                self.districtName = input("Please enter the district name:")

            def getDistrictName(self):
                return self.districtName

            class PostOffice:
                def __init__(self):
                    pass

                def setPostOfficeName(self):
                    self.postOfficeName = input("Please enter the post office name:")

                def getPostOfficeName(self):
                    return self.postOfficeName

                class Village:
                    def __init__(self):
                        self.po = Country().State().District().PostOffice()
                        self.ds = Country().State().District()
                        self.st = Country().State()
                        self.cty = Country()
                        self.cty.setCountry()
                        self.st.setState()
                        self.ds.setDistrictName()
                        self.po.setPostOfficeName()
                        self.setVillageName()

                    def setVillageName(self):
                        self.villageName = input("Please enter the village name:")

                    def getVillageName(self):
                        return self.villageName

                    def getFullDetails(self):
                        print("Village {} is in the {} post office of district {} of state {} in country {}."
                        .format(self.villageName, self.po.getPostOfficeName(), self.ds.getDistrictName(), self.st.getState(), self.cty.getCountry()))

v = Country().State().District().PostOffice().Village()
v.getFullDetails()