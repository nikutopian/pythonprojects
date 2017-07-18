# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSmallest(self, root):
        while root is not None and root.left is not None:
            root = root.left
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """

        if root is None:
            return None

        if root.val == key:
            if root.left is None:
                newroot = root.right
                del root
                return newroot

            if root.right is None:
                newroot = root.left
                del root
                return newroot

            newnode = self.findSmallest(root.right)
            root.val = newnode.val
            root.right = self.deleteNode(root.right, newnode.val)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

a = Solution()

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

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

a = Solution()
input = createtree([5,3,6,2,4,None,7], 0)
inorder(input)
print("------")
output = a.deleteNode(input, 0)
inorder(output)

