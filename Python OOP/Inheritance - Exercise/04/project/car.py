from .vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power) -> None:
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION