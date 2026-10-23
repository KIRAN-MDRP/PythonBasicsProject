class Vehicle:
    def __init__(self):
        pass
    def getVehicleName(self):
        vehicle_name = input("Enter vehicle name: ")
        return vehicle_name

class TwoWheeler(Vehicle):
    def __init__(self):
        pass
    def getVehicleWheels(self):
        return 2

class RoyalEnfield(TwoWheeler):
    def __init__(self):
        pass

    def getVehicleDetails(self):
        vehicle_name = self.getVehicleName()
        print("Vehicle name is: {} and it is {} wheeler ".format(vehicle_name, self.getVehicleWheels()))

re = RoyalEnfield()
re.getVehicleDetails()


