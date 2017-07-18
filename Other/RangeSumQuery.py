class NumMatrix(object):

    def updatemat(self, row, col, val):

        delta = val - self.nums[row][col]
        self.nums[row][col] = val

        i = row + 1
        while (i <= self.m):
            j = col + 1
            while (j <= self.n):
                self.cummatrix[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def summat(self, row, col):

        sumval = 0
        i = row
        while (i > 0):
            j = col
            while (j > 0):
                sumval += self.cummatrix[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return sumval



    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        if self.m <= 0:
            return
        self.n = len(matrix[0])

        self.nums = [[0] * self.n for _ in range(self.m)]
        self.cummatrix = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        # for i in range(self.m):
        #     for j in range(self.n):
        #         self.cummatrix[i][j] = self.matrix[i][j]
        #         if i > 0:
        #             self.cummatrix[i][j] += self.cummatrix[i-1][j]
        #         if j > 0:
        #             self.cummatrix[i][j] += self.cummatrix[i][j-1]
        #         if i > 0 and j > 0:
        #             self.cummatrix[i][j] -= self.cummatrix[i-1][j-1]

        for i in range(self.m):
            for j in range(self.n):
                self.updatemat(i,j,matrix[i][j])



    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        # self.matrix[row][col] = val
        # for i in range(row, self.m):
        #     for j in range(col, self.n):
        #         self.cummatrix[i][j] += val

        self.updatemat(row, col, val)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        # sumval = 0
        # for i in range(row1, row2+1):
        #     for j in range(col1, col2+1):
        #         sumval += self.matrix[i][j]
        #
        # return sumval

        # return self.cummatrix[row2][col2] + self.cummatrix[row1-1][col1-1] - self.cummatrix[row2][col1-1] - self.cummatrix[row1-1][col2]

        return self.summat(row2+1, col2+1) \
                + self.summat(row1, col1) \
                - self.summat(row2+1, col1) \
                - self.summat(row1, col2+1)





        

class BIT:
    def __init__(self):
        self.count = 0

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

a = NumMatrix(matrix)
print(a.sumRegion(2,1,4,3))
a.update(3,2,2)
print(a.sumRegion(2,1,4,3))


a = NumMatrix([[1]])
print(a.sumRegion(0,0,0,0))
a.update(0,0,-1)
print(a.sumRegion(0,0,0,0))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)