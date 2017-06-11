# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys

class Solution(object):
    def isvalid(self, root, minval, maxval):
        if root is None:
            return True

        if root.val < minval or root.val > maxval:
            return False

        return self.isvalid(root.left, minval, root.val - 1) and \
            self.isvalid(root.right, root.val + 1, maxval)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isvalid(root, -1 * (sys.maxsize - 1), sys.maxsize)


def createtree(vallist, index):
    l = len(vallist)
    if l <= index:
        return None
    if vallist[index] is None:
        return None

    node = TreeNode(vallist[index])
    node.left = createtree(vallist, index * 2 + 1)
    node.right = createtree(vallist, index * 2 + 2)
    return node

a = Solution()
print(a.isValidBST(createtree([2,0,3], 0)))
print(a.isValidBST(createtree([10,5,15,None,None,6,20], 0)))
print(a.isValidBST(createtree([10,5,15,None,None,10,20], 0)))
print(a.isValidBST(createtree([10,5,15,None,None,11,20], 0)))
print(a.isValidBST(createtree([10,5,15,None,None,12,20], 0)))
