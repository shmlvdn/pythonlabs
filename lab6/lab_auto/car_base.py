class Car:
    def __init__(self, name, fuel_per_km_empty, max_load):
        self.name = name
        self.fuel_per_km_empty = fuel_per_km_empty  # расход без загрузки (л/км)
        self.max_load = max_load  # максимальная загрузка в кг


class PassengerCar(Car):
    def __init__(self):
        super().__init__("Легковой", 0.08, 500) 

class Truck(Car):
    def __init__(self):
        super().__init__("Грузовой", 0.18, 5000)

class Bus(Car):
    def __init__(self):
        super().__init__("Пассажирский", 0.12, 1500)

# супер заполняет три поля конкретными цифрами