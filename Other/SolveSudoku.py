__author__ = 'user'


class Solution:
    def __init__(self):
        self.horizontals = [0] * 9
        self.verticals = [0] * 9
        self.blocks = [0] * 9

    def initVariables(self, board):
        r = range(len(board))
        for i in r:
            for j in r:
                if board[i][j] != '.':
                    val = int(board[i][j])
                    self.horizontals[i] |= (1 << val)
                    self.verticals[j] |= (1 << val)
                    b = (i // 3) + (j // 3)
                    self.blocks[b] != (1 << val)

    def solveSudoku(self, board):
        self.initVariables(board)
        print(self.horizontals)
        print(self.verticals)
        print(self.blocks)
        r = range(len(board))
        for i in r:
            for j in r:
                if board[i][j] == '.':
                    b = (i // 3) + (j // 3)
                    self.horizontals[i] | self.verticals[j] | self.blocks[b]


a = [0] * 9
print(a)



