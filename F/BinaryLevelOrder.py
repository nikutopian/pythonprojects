# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []
        queue = []
        queue.append((root, 0))

        while len(queue) > 0:
            topnode,depth = queue.pop(0)
            if len(output) == depth:
                output.append([])
            output[depth].append(topnode.val)
            if topnode.left is not None:
                queue.append((topnode.left, depth + 1))
            if topnode.right is not None:
                queue.append((topnode.right, depth + 1))

        return output

a = Solution()
arr = [3,9,20,None,None,15,7]

def const_tree(arr, index):
    if index >= len(arr) or arr[index] == None:
        return None
    node = TreeNode(arr[index])
    node.left = const_tree(arr, index * 2 + 1)
    node.right = const_tree(arr, index * 2 + 2)
    return node

node = const_tree(arr, 0)
print(a.levelOrder(node))

