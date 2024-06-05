# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")

# Child class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def refuel(self):
        print(f"Refueling the {self.brand} {self.model} with {self.fuel_type}")

# Child class inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity = engine_capacity

    def ride(self):
        print(f"Riding in the city on  {self.brand} {self.model}")

# Create instances of the classes
car = Car("Toyota", "Camry", "Petrol")
motorcycle = Motorcycle("Honda", "CBR600RR", "600cc")

# Use the inherited methods
car.drive()
car.refuel()

motorcycle.drive()
motorcycle.ride()