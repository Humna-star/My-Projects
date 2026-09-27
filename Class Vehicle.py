#create class
class Vehicle:

    #create init method
    def __init__(self, max_speed, mileage):

        #bind the arguement
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = Vehicle(240, 18)

#acess the vehicle inside this method
print("model max speed:", modelX.max_speed)
print("model mileage:", modelX.mileage)