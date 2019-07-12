#Creating and displaying inheritance and polymorphism with a car creating program

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, str(self.mpg))
#Sets condition of car to used when called
    def drive_car(self):
        self.condition="used"
#Creating new child class
class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        self.model=model
        self.color=color
        self.mpg=mpg
#Overriding Parent function declarations and local variable 
    def drive_car(self):
        self.condition="like new"
#Instance of Parent Class
my_car = Car("DeLorean", "silver", 88)
#Instance of Child Class
my_car=ElectricCar("molten salt","Porsche", "black", 45)

print my_car.display_car()
