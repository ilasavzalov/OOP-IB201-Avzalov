from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Order:
    total: float

@dataclass
class Customer:
    kind: str


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, order: Order, customer: Customer) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total


class VipDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.9


class EmployeeDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.8


class BlackFridayDiscount(DiscountStrategy):
    def apply(self, order: Order, customer: Customer) -> float:
        return order.total * 0.5


def apply_discount(order: Order, customer: Customer) -> float:
    discounts = {
        "regular": RegularDiscount(),
        "vip": VipDiscount(),
        "employee": EmployeeDiscount(),
        "black_friday": BlackFridayDiscount(),
    }
    
    strategy = discounts.get(customer.kind, RegularDiscount())
    return strategy.apply(order, customer)
