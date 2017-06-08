# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getminmax(self, root, index):
        if root is None:
            return (index+1, index-1)

        minmax1 = self.getminmax(root.left, index - 1)
        minmax2 = self.getminmax(root.right, index + 1)

        return (min(minmax1[0], minmax2[0]), max(minmax1[1], minmax2[1]))

    def internalVerticalOrder(self, root, index, out_list):
        if root is None:
            return

        queue = []
        queue.append((root, index))

        while len(queue) > 0:
            node, index = queue.pop(0)
            out_list[index].append(node.val)
            if node.left is not None:
                queue.append((node.left, index - 1))
            if node.right is not None:
                queue.append((node.right, index + 1))

    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        minmax = self.getminmax(root, 0)
        rangelen = minmax[1] - minmax[0] + 1
        out_list = [[] for _ in range(rangelen)]

        self.internalVerticalOrder(root, 0 - minmax[0], out_list)
        return out_list



a = Solution()
arr = [3,9,8,4,0,1,7,None, None, None,2,5]

def const_tree(arr, index):
    if index >= len(arr) or arr[index] == None:
        return None
    node = TreeNode(arr[index])
    node.left = const_tree(arr, index * 2 + 1)
    node.right = const_tree(arr, index * 2 + 2)
    return node

node = const_tree(arr, 0)


# print(a.getminmax(node3, 0))
# print(a.getminmax(node7, 0))
# print(a.getminmax(node12, 0))
# print(a.getminmax(node15, 0))
# print(a.getminmax(node20, 0))

print(a.verticalOrder(node))

