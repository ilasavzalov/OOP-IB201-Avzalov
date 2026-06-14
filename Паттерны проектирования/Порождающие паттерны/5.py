class GameSettings:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Инициализация настроек по умолчанию
            cls._instance.volume = 50
            cls._instance.difficulty = "Normal"
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        return cls()


settings1 = GameSettings.get_instance()
settings2 = GameSettings.get_instance()

print(settings1 is settings2)  # True

settings1.volume = 70
settings1.difficulty = "Hard"

print(settings2.volume)        # 70
print(settings2.difficulty)    # Hard
