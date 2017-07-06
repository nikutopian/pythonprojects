class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def topo_sort(self, u, topo_list):
        visited = [0] * self.V
        no_cycles = True
        while (sum(visited) < self.V * 2):
            no_cycles = self.depth_search(u, visited, topo_list)
            if not no_cycles:
                return False
            for i in range(self.V):
                if visited[i] == 0:
                    u = i
                    break
        return no_cycles

    def depth_search(self, u, visited, topo_list):
        visited[u] = 1
        no_cycles = True
        for v in self.adj[u]:
            if visited[v] == 0:
                if not self.depth_search(v, visited, topo_list):
                    no_cycles = False
                    break
            elif visited[v] == 1:
                return False
        visited[u] = 2
        topo_list.insert(0, u)

        return no_cycles


class Solution(object):
    def getdiff(self, word1, word2):
        m = min(len(word1), len(word2))
        for i in range(m):
            if word1[i] != word2[i]:
                return word1[i], word2[i]
        return None,None

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        all_chars = list(set("".join(words)))
        all_chars_map = {v:k for k,v in enumerate(all_chars)}
        l = len(all_chars)
        graph = Graph(l)

        for i in range(0, len(words)-1):
            c1,c2 = self.getdiff(words[i], words[i+1])
            if c1 is not None:
                graph.add_edge(all_chars_map[c1], all_chars_map[c2])

        topo_list = []

        no_cycles = graph.topo_sort(all_chars_map[words[0][0]], topo_list)

        if not no_cycles:
            return ""

        ordered_list = [all_chars[i] for i in topo_list]

        return "".join(ordered_list)



a = Solution()
print(
    a.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])
)

print(a.alienOrder([
  "z",
  "x"
]))

print(a.alienOrder([
  "z",
  "x",
  "z"
]))

print(a.alienOrder(["zy","zx"]))




