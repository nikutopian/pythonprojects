__author__ = 'user'


class Solution:
    def __init__(self):
        self.horizontals = [0] * 9
        self.verticals = [0] * 9
        self.blocks = [0] * 9

        self.digits = '123456789'
        rows = 'ABCDEFGHI'
        cols = self.digits

        self.squares = self.cross(rows, cols)
        self.unitlist = ([self.cross(rows, c) for c in cols] +
                    [self.cross(r, cols) for r in rows] +
                    [self.cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.squares)

        print(self.peers)


    def assign(self, values, s, d):
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values

        return False

    def eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        if len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False

        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            if len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False

        return values

    def parse_grid(self, board):
        values = dict((s, self.digits) for s in self.squares)
        for s,d in self.grid_values(board).items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def grid_values(self, board):
        chars = [c for c in board if c in self.digits or c in '0.']
        assert(len(chars) == 81)
        return dict(zip(self.squares, chars))

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

    def cross(self, A, B):
        return [a+b for a in A for b in B]




a = Solution()





