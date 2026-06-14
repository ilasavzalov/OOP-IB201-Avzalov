from abc import ABC, abstractmethod


# Абстрактный класс Car
class Car(ABC):
    @abstractmethod
    def drive(self) -> str:
        pass
    
    @abstractmethod
    def get_specs(self) -> dict:
        pass


# Конкретные классы автомобилей
class ElectricCar(Car):
    def __init__(self):
        self.battery_capacity = "100 kWh"
        self.power = "300 л.с."
        self.range = "500 км"
    
    def drive(self) -> str:
        return "Driving an electric car."
    
    def get_specs(self) -> dict:
        return {
            "type": "Electric",
            "battery": self.battery_capacity,
            "power": self.power,
            "range": self.range
        }


class PetrolCar(Car):
    def __init__(self):
        self.engine_volume = "2.0 л"
        self.power = "200 л.с."
        self.fuel_consumption = "7 л/100 км"
    
    def drive(self) -> str:
        return "Driving a petrol car."
    
    def get_specs(self) -> dict:
        return {
            "type": "Petrol",
            "engine_volume": self.engine_volume,
            "power": self.power,
            "fuel_consumption": self.fuel_consumption
        }


class HybridCar(Car):
    def __init__(self):
        self.engine_volume = "1.5 л"
        self.battery_capacity = "50 kWh"
        self.power = "250 л.с."
        self.fuel_consumption = "3.5 л/100 км"
    
    def drive(self) -> str:
        return "Driving a hybrid car."
    
    def get_specs(self) -> dict:
        return {
            "type": "Hybrid",
            "engine_volume": self.engine_volume,
            "battery": self.battery_capacity,
            "power": self.power,
            "fuel_consumption": self.fuel_consumption
        }


# Абстрактная фабрика
class CarFactory(ABC):
    @abstractmethod
    def produce_car(self) -> Car:
        pass
    
    @abstractmethod
    def produce_sport_car(self) -> Car:
        pass  # Дополнительный метод для демонстрации


# Конкретные фабрики
class ElectricCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return ElectricCar()
    
    def produce_sport_car(self) -> Car:
        return ElectricSportCar()


class PetrolCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return PetrolCar()
    
    def produce_sport_car(self) -> Car:
        return PetrolSportCar()


class HybridCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return HybridCar()
    
    def produce_sport_car(self) -> Car:
        return HybridSportCar()


# Дополнительные классы спортивных автомобилей
class ElectricSportCar(ElectricCar):
    def __init__(self):
        super().__init__()
        self.battery_capacity = "150 kWh"
        self.power = "600 л.с."
        self.range = "400 км"
    
    def drive(self) -> str:
        return "Driving an electric SPORT car!"


class PetrolSportCar(PetrolCar):
    def __init__(self):
        super().__init__()
        self.engine_volume = "4.0 л"
        self.power = "500 л.с."
        self.fuel_consumption = "15 л/100 км"
    
    def drive(self) -> str:
        return "Driving a petrol SPORT car!"


class HybridSportCar(HybridCar):
    def __init__(self):
        super().__init__()
        self.engine_volume = "3.0 л"
        self.battery_capacity = "100 kWh"
        self.power = "550 л.с."
        self.fuel_consumption = "8 л/100 км"
    
    def drive(self) -> str:
        return "Driving a hybrid SPORT car!"


# Клиентский код
def produce_and_test_cars(factory: CarFactory) -> None:
    print(f"\n--- Testing {factory.__class__.__name__} ---")
    
    # Обычный автомобиль
    car = factory.produce_car()
    print(car.drive())
    print(f"Specs: {car.get_specs()}")
    
    # Спортивный автомобиль
    sport_car = factory.produce_sport_car()
    print(sport_car.drive())
    print(f"Specs: {sport_car.get_specs()}")


# Пример использования
if __name__ == "__main__":
    electric_factory = ElectricCarFactory()
    petrol_factory = PetrolCarFactory()
    hybrid_factory = HybridCarFactory()
    
    # Тестирование
    produce_and_test_cars(electric_factory)
    produce_and_test_cars(petrol_factory)
    produce_and_test_cars(hybrid_factory)
    
    # Простое использование как в условии
    print("\n" + "="*50)
    print("Простое использование:")
    
    electric_car = electric_factory.produce_car()
    petrol_car = petrol_factory.produce_car()
    hybrid_car = hybrid_factory.produce_car()
    
    print(electric_car.drive())
    print(petrol_car.drive())
    print(hybrid_car.drive())
