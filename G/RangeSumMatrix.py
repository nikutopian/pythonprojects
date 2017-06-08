__author__ = 'user'

class NumMatrix:
    def __init__(self):
        self.tree = []
        self.nums = []
        self.m = 0
        self.n = 0

    def init(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.tree = [[0] * (n+1) for _ in range(m+1)]
        self.nums = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.update(i,j,matrix[i][j])

    def update(self, row, col, val):
        if (self.m == 0 or self.n == 0):
            return
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        i = row + 1
        j = col + 1
        while (i <= self.m):
            while (j <= self.n):
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)


    def sumRegion(self, row1, col1, row2, col2):
        if (self.m == 0 or self.n == 0):
            return
        return  self.mysum(row2+1, col2+1) + \
                self.mysum(row1, col1) - \
                self.mysum(row1, col2+1) - \
                self.mysum(row2+1, col1)

    def mysum(self, row, col):
        msum = 0
        i = row
        j = col
        while (i>0):
            while (j>0):
                msum += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)

        return msum
