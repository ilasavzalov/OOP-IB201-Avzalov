import json
from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str


class OrderLoader:
    @staticmethod
    def load(json_path: str) -> List[dict]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)


class OrderParser:
    @staticmethod
    def parse(raw_orders: List[dict]) -> List[Order]:
        orders = []
        for item in raw_orders:
            if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")
            orders.append(Order(item["id"], float(item["price"]), int(item["qty"]), item["email"]))
        return orders


class OrderCalculator:
    @staticmethod
    def calculate_total(orders: List[Order]) -> float:
        return sum(o.price * o.qty for o in orders)


class OrderReportFormatter:
    @staticmethod
    def format(orders: List[Order], total: float) -> str:
        return f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"


class EmailSender:
    @staticmethod
    def send(to: str, subject: str, body: str) -> None:
        print(f"[EMAIL to={to}] {subject}\n{body}")


class OrderReportService:
    def __init__(self, email_sender=EmailSender()):
        self.email_sender = email_sender
    
    def make_and_send_report(self, json_path: str, send_email: bool = True) -> str:
        # 1) load
        raw = OrderLoader.load(json_path)
        
        # 2) validate + parse
        orders = OrderParser.parse(raw)
        
        # 3) calc
        total = OrderCalculator.calculate_total(orders)
        
        # 4) format
        report = OrderReportFormatter.format(orders, total)
        
        # 5) send
        if send_email:
            for o in orders:
                self.email_sender.send(o.customer_email, "Your order report", report)
        
        return report
