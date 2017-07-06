# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    # def serialize(self):
    #     arr = [self.label] + [node.label for node in self.neighbors] + ['#']
    #     for node in self.neighbors:
    #         arr += node.serialize()
    #     return arr




class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodelist = []
        if node is None:
            return None

        visitednodes = {}
        returnnode = UndirectedGraphNode(node.label)
        visitednodes[node.label] = returnnode

        for oldneighbor in node.neighbors:
            nodelist.append((returnnode, oldneighbor))

        while len(nodelist) > 0:
            newnode,oldneighbor = nodelist.pop(0)
            if not oldneighbor.label in visitednodes:
                newneighbornode = UndirectedGraphNode(oldneighbor.label)
                visitednodes[oldneighbor.label] = newneighbornode
                for oldneighbor in oldneighbor.neighbors:
                    nodelist.append((newneighbornode, oldneighbor))
            else:
                newneighbornode = visitednodes[oldneighbor.label]

            newnode.neighbors.append(newneighbornode)

        return returnnode

a = Solution()
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node3 = UndirectedGraphNode(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node3]
node3.neighbors = [node3]
print(node1)
retnode = a.cloneGraph(node1)
print(retnode)


        