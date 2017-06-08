# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longest(self, root, lensofar):
        if root == None:
            return 0

        long = lensofar + 1

        if root.left is not None:
            long = max(long, self.longest(root.left, lensofar + 1 if root.val + 1 == root.left.val else 0))
        if root.right is not None:
            long = max(long, self.longest(root.right, lensofar + 1 if root.val + 1 == root.right.val else 0))

        return long


    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.longest(root, 0)



a = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node1.right = node3
node3.left = node2
node3.right = node4
node4.right = node5
print(a.longestConsecutive(node1))

node1 = TreeNode(1)
node2 = TreeNode(2)
node22 = TreeNode(2)
node3 = TreeNode(3)
node22.right = node3
node3.left = node2
node2.left = node1
print(a.longestConsecutive(node22))
