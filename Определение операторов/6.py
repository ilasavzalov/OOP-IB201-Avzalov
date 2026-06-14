class SparseArray:
    def __init__(self):
        self.data = {}
    
    def __setitem__(self, key, value):
        if value != 0:
            self.data[key] = value
        elif key in self.data:
            del self.data[key]
    
    def __getitem__(self, key):
        return self.data.get(key, 0)

print("Пример1")
arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
print()

print("Пример2")
arr = SparseArray()
arr[10] = 123
for i in range(8, 13):
    print('arr[{}] = {}'.format(i, arr[i]))
print()

print("Пример3")
def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)
