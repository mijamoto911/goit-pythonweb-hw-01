from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Car):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")
        
class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass

class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")



class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU Spec")

def main():
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_car.start_engine()
    us_motorcycle.start_engine()

    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Porsche", "Carrera-911")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "S 1000 RR")
    eu_car.start_engine()
    eu_motorcycle.start_engine()

if __name__ == "__main__":
    main()

