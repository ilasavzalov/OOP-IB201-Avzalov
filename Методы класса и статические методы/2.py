class Password:
    @staticmethod
    def is_strong(p: str) -> bool:
        if len(p) < 8:
            return False
        
        has_digit = False
        has_upper = False
        has_lower = False
        
        for char in p:
            if char.isdigit():
                has_digit = True
            elif char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
        
        return has_digit and has_upper and has_lower

print("Пример")
print(Password.is_strong('qwerty'))
print(Password.is_strong('Qwerty12'))
print(Password.is_strong('QWERTY12'))
print(Password.is_strong('Qwerty123'))



