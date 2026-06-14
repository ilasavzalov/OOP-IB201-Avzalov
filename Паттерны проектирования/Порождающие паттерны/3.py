from abc import ABC, abstractmethod

# Компоненты автомобиля
class Engine:
    def __init__(self, engine_type: str):
        self.engine_type = engine_type
    
    def __str__(self):
        return self.engine_type

class Transmission:
    def __init__(self, transmission_type: str):
        self.transmission_type = transmission_type
    
    def __str__(self):
        return self.transmission_type

class Body:
    def __init__(self, body_type: str):
        self.body_type = body_type
    
    def __str__(self):
        return self.body_type


# Класс автомобиля
class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.color = None
        self.engine = None
        self.transmission = None
        self.body = None
    
    def __str__(self):
        return f"{self.brand} {self.model}, цвет: {self.color}, {self.body} кузов, {self.engine} двигатель, {self.transmission} КПП"


# Абстрактный строитель
class CarBuilder(ABC):
    def __init__(self):
        self.car = Car()
    
    @abstractmethod
    def set_brand(self):
        pass
    
    @abstractmethod
    def set_model(self):
        pass
    
    @abstractmethod
    def set_color(self):
        pass
    
    @abstractmethod
    def set_engine(self):
        pass
    
    @abstractmethod
    def set_transmission(self):
        pass
    
    @abstractmethod
    def set_body(self):
        pass
    
    def get_car(self):
        return self.car


# Конкретные строители
class SedanBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "Toyota"
    
    def set_model(self):
        self.car.model = "Camry"
    
    def set_color(self):
        self.car.color = "Silver"
    
    def set_engine(self):
        self.car.engine = Engine("Petrol 2.5L")
    
    def set_transmission(self):
        self.car.transmission = Transmission("Automatic 8-speed")
    
    def set_body(self):
        self.car.body = Body("Sedan")


class SUVBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "BMW"
    
    def set_model(self):
        self.car.model = "X5"
    
    def set_color(self):
        self.car.color = "Black"
    
    def set_engine(self):
        self.car.engine = Engine("Petrol 4.4L")
    
    def set_transmission(self):
        self.car.transmission = Transmission("Automatic 8-speed")
    
    def set_body(self):
        self.car.body = Body("SUV")


class SportsCarBuilder(CarBuilder):
    def set_brand(self):
        self.car.brand = "Porsche"
    
    def set_model(self):
        self.car.model = "911"
    
    def set_color(self):
        self.car.color = "Red"
    
    def set_engine(self):
        self.car.engine = Engine("Petrol 3.8L Turbo")
    
    def set_transmission(self):
        self.car.transmission = Transmission("PDK 8-speed")
    
    def set_body(self):
        self.car.body = Body("Sports")


# Директор
class CarDirector:
    def __init__(self, builder: CarBuilder):
        self.builder = builder
    
    def construct_car(self) -> Car:
        self.builder.set_brand()
        self.builder.set_model()
        self.builder.set_color()
        self.builder.set_engine()
        self.builder.set_transmission()
        self.builder.set_body()
        return self.builder.get_car()


# Пример использования
sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)

suv_builder = SUVBuilder()
director = CarDirector(suv_builder)
suv = director.construct_car()
print("Создан внедорожник:", suv)

sports_builder = SportsCarBuilder()
director = CarDirector(sports_builder)
sports_car = director.construct_car()
print("Создан спорткар:", sports_car)
