__author__ = 'user'

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        assert u < self.V
        assert v < self.V

        self.adj[u].append(v)


