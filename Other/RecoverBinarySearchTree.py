__author__ = 'user'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ob = []

    def traverse(self, root, prev):
        if root is None:
            return None

        lprev = self.traverse(root.left, prev)

        if lprev is not None:
            prev = lprev

        if prev is not None and root.val < prev.val:
            if len(self.ob) == 0:
                self.ob.append(prev)
                self.ob.append(root)
            else:
                self.ob.append(root)

        prev = root

        rprev = self.traverse(root.right, prev)

        if rprev is not None:
            prev = rprev

        return prev

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # self.isAdjacentSwap(root)
        # if (len(self.outoforderobjects)) == 4:
        #     self.outoforderobjects[0].val, self.outoforderobjects[3].val = \
        #         self.outoforderobjects[3].val, self.outoforderobjects[0].val
        # elif len(self.outoforderobjects) == 2:
        #     self.outoforderobjects[0].val, self.outoforderobjects[1].val = \
        #         self.outoforderobjects[1].val, self.outoforderobjects[0].val

        self.traverse(root, None)

        if len(self.ob) > 1:
            left = self.ob[0]
            right = self.ob[1]
            if len(self.ob) > 2:
                right = self.ob[2]

            left.val, right.val = right.val, left.val


        return

# head = TreeNode(10)
# head.left = TreeNode(8)
# head.right = TreeNode(20)
# head.left.left = TreeNode(2)
# head.left.right = TreeNode(5)

head = TreeNode(10)
head.left = TreeNode(5)
head.right = TreeNode(8)
head.left.left = TreeNode(2)
head.left.right = TreeNode(20)

a = Solution()
# print(a.isAdjacentSwap(head))
a.inorder(head)
a.recoverTree(head)
a.inorder(head)