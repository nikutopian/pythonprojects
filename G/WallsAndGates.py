class Solution(object):
    def breadth_search(self, rooms, posval, nonzeropositions):
        i = posval[0]
        j = posval[1]
        
        for inci, incj in [(-1,0), (0,-1), (1,0), (0,1)]:
            newi = i + inci
            newj = j + incj
            if newi >= 0 and newi < len(rooms) and newj >= 0 and newj < len(rooms[0]):
                print((newi, newj))
                if rooms[newi][newj] > rooms[i][j] + 1:
                    rooms[newi][newj] = rooms[i][j] + 1
                    nonzeropositions.append((newi, newj, rooms[i][j] + 1))



    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        zeropos = set()
        m = len(rooms)
        if m == 0:
            return
        n = len(rooms[0])

        nonzeropositions = []

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    nonzeropositions.append((i,j,0))

        while len(nonzeropositions) > 0:
            top = nonzeropositions.pop(0)
            self.breadth_search(rooms, top, nonzeropositions)

a = Solution()
INF = 2 ** 31 - 1
rooms = [[INF,  -1,  0,  INF],
[INF, INF, INF,  -1],
[INF, -1, INF,  -1],
[0,  -1, INF, INF]]

a.wallsAndGates(rooms)
print(rooms)
