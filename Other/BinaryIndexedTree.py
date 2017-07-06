class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.arr = [0] * (n + 1)

    def update(self, index, val):
        while index < self.n:
            self.arr[index] += val
            index += index & -index

    def search(self, index):
        sum = 0
        if index >= self.n:
            return
        while index > 0:
            sum += self.arr[index]
            index -= index & -index
        return sum


a = [3, 4, 5, 6, 2, 1, 8, 9 ,10, 2, 3, -5, 23, -12]
b = BIT(len(a))
for index,item in enumerate(a):
    b.update(index + 1, item)
print(b.search(len(a)))
print(b.search(1))
print(b.search(2))
print(b.search(3))

