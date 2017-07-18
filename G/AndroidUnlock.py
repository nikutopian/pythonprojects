# 0 1 2
# 3 4 5
# 6 7 8

class Solution(object):
    def __init__(self):
        jump = [[0] * 9 for _ in range(9)]

        grid = [list(range(i, i+3)) for i in range(0,7,3)]
        print(grid)

        for i in range(3):
            for j in range(3):
                for inci in range(-2,2+1,2):
                    for incj in range(-2,2+1,2):
                        ri = i + inci
                        rj = j + incj
                        if 0 <= ri and ri <= 2 and 0 <= rj and rj <= 2:
                            a = grid[i][j]
                            b = grid[ri][rj]
                            mid = grid[(ri + i) // 2][(rj + j) // 2]
                            jump[a][b] = jump[b][a] = mid

        self.jump = jump

    def getPatterns(self, visit, cur, left):
        if left == 0:
            return 1
        if left < 0:
            return 0
        ways = 0
        visit[cur] = True
        for i in range(9):
            if visit[i] == False and \
                (self.jump[i][cur] == 0 or \
                    visit[self.jump[i][cur]] == True):
                ways += self.getPatterns(visit, i, left - 1)

        visit[cur] = False

        return ways

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visit = [False] * 9


        ways1 = 0
        for i in range(m,n+1):
            ways1 += 4 * self.getPatterns(visit, 0, i-1)
            ways1 += 4 * self.getPatterns(visit, 1, i-1)
            ways1 += self.getPatterns(visit, 4, i-1)

        return ways1

a = Solution()
print(a.numberOfPatterns(1,1))
print(a.numberOfPatterns(1,2))