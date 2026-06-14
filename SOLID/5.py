from abc import ABC, abstractmethod
from typing import List

class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, text: str) -> None:
        pass


class EmailNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[EMAIL to={to}] {text}")


class SmsNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[SMS to={to}] {text}")


class PushNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[PUSH to={to}] {text}")


class FakeNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[FAKE] Would send to {to}: {text}")


class NotificationService:
    def __init__(self, notifiers: List[Notifier]):
        self.notifiers = notifiers
    
    def notify(self, user_email: str, user_phone: str, text: str) -> None:
        for notifier in self.notifiers:
            if isinstance(notifier, EmailNotifier):
                notifier.send(user_email, text)
            elif isinstance(notifier, SmsNotifier):
                notifier.send(user_phone, text)
            elif isinstance(notifier, PushNotifier):
                notifier.send(user_phone, text)
            else:
                notifier.send("default", text)



email_notifier = EmailNotifier()
sms_notifier = SmsNotifier()
push_notifier = PushNotifier()
fake_notifier = FakeNotifier()

service = NotificationService([email_notifier, sms_notifier, push_notifier])
service.notify("user@example.com", "+123456789", "Hello!")

test_service = NotificationService([fake_notifier])
test_service.notify("test@example.com", "+000000000", "Test message")
