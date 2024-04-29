class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = None
        self.mileage = 0

    def set_color(self, color):
        self.color = color
        return self  # Return self for chaining

    def drive(self, miles):
        self.mileage += miles
        return self  # Return self for chaining

    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage} miles")

# usage of method chaining
my_car = Car("Toyota", "Corolla")
my_car.set_color("Blue").drive(100).display_info()
