class ReversedList:
    def __init__(self, lst):
        self.lst = lst
    
    def __len__(self):
        return len(self.lst)
    
    def __getitem__(self, index):
        return self.lst[-(index + 1)]

print("Пример1")
rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])
print()

print("Пример2")
rl = ReversedList([])
print(len(rl))
print()

print("Пример3")
rl = ReversedList([10])
print(len(rl))
print(rl[0])
