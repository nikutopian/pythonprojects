__author__ = 'user'

from collections import defaultdict
from queue import *

class Graph:
    def __init__(self, v):
        self.V = v
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        assert u < self.V
        assert v < self.V

        self.adj[u].append(v)


    def is_bipartite_util(self, s, visited):
        q = Queue()
        colorQueue = Queue()
        q.put(s)
        colorQueue.put(1)



        while not q.empty():
            s = q.get()
            c = colorQueue.get()

            if visited[s] == 0:
                visited[s] = c
                for i in self.adj[s]:
                    q.put(i)
                    colorQueue.put(3 - c)
            elif visited[s] != c:
                return False

        return True

    def is_bipartite(self):
        visited = [0] * len(self.adj.items())

        for i in range(len(self.adj.items())):
            if visited[i] == 0:
                if not self.is_bipartite_util(i, visited):
                    return False

        return True


