import random

class Solution(object):
    def validateSet(self, cellset):
        cellnumset = [int(x) for x in cellset if x != '.']
        if len(cellnumset) != len(set(cellnumset)) or (len(cellnumset) > 0 and (max(cellnumset) > 9 or min(cellnumset) < 1)):
            return False
        return True

    def row(self, board, i):
        return board[i]

    def column(self, board, i):
        return [row[i] for row in board]

    def block(self, board, i):
        m = i // 3
        n = i % 3
        blockcells = []
        for k in range(m*3, m*3+3):
            for j in range(n*3, n*3+3):
                blockcells.append(board[k][j])
        return blockcells


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            ret = self.validateSet(self.row(board, i)) and self.validateSet(self.column(board, i)) and self.validateSet(self.block(board, i))
            if not ret:
                return False

        return True

a = Solution()

board = [['.'] * 9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if random.random() < 0.3:
            board[i][j] = str(random.randint(0,9))

board2 = [['5', '.', '.', '.', '.', '.', '7', '.', '.'],
          ['4', '.', '.', '.', '.', '.', '9', '.', '.'],
          ['.', '.', '5', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '2', '.', '.'],
          ['.', '.', '.', '1', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.', '.', '.']]


print(a.isValidSudoku(board2))
