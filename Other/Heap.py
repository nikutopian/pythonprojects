class Heap:
    def __init__(self, capacity, compfunc):
        self.capacity = capacity
        self.compfunc = compfunc
        self.arr = [-1] * capacity
        self.count = 0

    def insert(self, item):
        if self.count == self.capacity:
            return False
        self.arr[self.count] = item
        self.count += 1
        self.heapify_from_bottom(self.count - 1)

    def pop(self):
        if self.count == 0:
            return None
        top = self.arr[0]
        self.arr[0] = self.arr[self.count - 1]
        self.count -= 1
        self.heapify_from_top(0)
        return top

    def heapify_from_top(self, index):
        minindex = index
        leftindex = 2 * index + 1
        rightindex = 2 * index + 2
        if leftindex < self.count and self.compfunc(self.arr[minindex], self.arr[leftindex]):
            minindex = leftindex
        if rightindex < self.count and self.compfunc(self.arr[minindex], self.arr[rightindex]):
            minindex = rightindex
        if minindex != index:
            self.arr[minindex], self.arr[index] = self.arr[index], self.arr[minindex]
            self.heapify_from_top(minindex)

    def heapify_from_bottom(self, index):
        parentindex = (index - 1) // 2
        if parentindex != index and self.compfunc(self.arr[parentindex], self.arr[index]):
            self.arr[parentindex], self.arr[index] = self.arr[index], self.arr[parentindex]
            self.heapify_from_bottom(parentindex)


