from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read_data(self):
        pass
    
# Адаптируемый класс 1: работа с файлом
class FileDataSource(DataSource):
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()

# Адаптируемый класс 2: работа с БД (несовместимый интерфейс)
class DatabaseDataSource:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    def fetch_data(self):
        # Имитация чтения из БД
        return f"Data from database using {self.connection_string}"
    
# Адаптер
class DatabaseAdapter(DataSource):
    def __init__(self, database_source: DatabaseDataSource):
        self.database_source = database_source
    def read_data(self):
        # Адаптируем вызов fetch_data к интерфейсу read_data
        return self.database_source.fetch_data()

# Пример использования
# Создаем файл для теста
with open("data.txt", 'w', encoding='utf-8') as f:
    f.write("Data from file")
file_source = FileDataSource("data.txt")
print(file_source.read_data())  # Data from file
database_source = DatabaseDataSource("database_connection_string")
database_adapter = DatabaseAdapter(database_source)
print(database_adapter.read_data())  # Data from database using database_connection_string
