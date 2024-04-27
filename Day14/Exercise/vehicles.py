class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        return f"{self.make} {self.model} starting..."

class ElectricVehicle:
    def __init__(self, range_per_charge):
        self.range = range_per_charge
    
    def charge(self):
        return "Charging the EV..."

class GasVehicle:
    def __init__(self, tank_size):
        self.tank = tank_size
    
    def refuel(self):
        return "Refueling the vehicle..."

class ElectricCar(Vehicle, ElectricVehicle):
    def __init__(self, make, model, year, range_per_charge):
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, range_per_charge)
    
    def start(self):
        return f"{self.make} {self.model} EV starting..."

class GCar(Vehicle, GasVehicle):  # Changed class name to 'GCar'
    def __init__(self, make, model, year, tank_size):  # Changed variable name 'tank_size' to 'tank'
        Vehicle.__init__(self, make, model, year)
        GasVehicle.__init__(self, tank_size)
    
    def start(self):
        return f"{self.make} {self.model} gas car starting..."

# Usage example
my_ev = ElectricCar("Tesla", "Model S", 2022, 350)
print(my_ev.start())
print(my_ev.charge())

my_gas_car = GCar("Toyota", "Corolla", 2023, 50)  # Using 'GCar' for GasCar instance
print(my_gas_car.start())
print(my_gas_car.refuel())
