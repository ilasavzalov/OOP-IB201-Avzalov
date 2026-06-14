from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None:
        pass


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass


class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None:
        pass


class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None:
        pass


class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)


class MultiFunctionPrinter(Printable, Scannable, Faxable, Copiable):
    def print(self, text: str) -> None:
        print(f"Printing: {text}")
    
    def scan(self) -> str:
        return "Scanned document"
    
    def fax(self, number: str) -> None:
        print(f"Faxing to {number}")
    
    def copy(self) -> None:
        print("Copying document")


# Клиентский код, зависящий только от Printable
def print_document(printer: Printable, text: str) -> None:
    printer.print(text)


simple = SimplePrinter()
multi = MultiFunctionPrinter()

print_document(simple, "Hello")
print_document(multi, "World")
