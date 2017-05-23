__author__ = 'user'

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
    
    def __dfs_util(self, u, visited, stack=None):
        visited[u] = True
        print(u)
        for v in self.adj[u]:
            if visited[v] == False:
                self.__dfs_util(v, visited)
        if stack is not None:
            stack.insert(0, u)
        
    def dfs(self, stack=None):
        visited = [False] * len(self.adj.items())
        for u,_ in self.adj.items():
            if visited[u] == False:
                self.__dfs_util(u, visited, stack)

    def topological_sort(self):
        stack = []
        self.dfs(stack)
        print(stack)
        


# g = Graph()
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
# g.dfs()

g = Graph()
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);
g.topological_sort()
