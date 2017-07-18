# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    def get_traversal_list(self, root, p, t_list):

        if root == None:
            return False

        if root == p:
            t_list.insert(0, root)
            return True

        is_correct = self.get_traversal_list(root.left, p, t_list) or \
            self.get_traversal_list(root.right, p, t_list)

        if is_correct:
            t_list.insert(0, root)
            return True

        return False





    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_list = []
        q_list = []

        self.get_traversal_list(root, p, p_list)
        self.get_traversal_list(root, q, q_list)

        m = min(len(p_list), len(q_list))

        lca = None

        for i in range(m):
            if p_list[i] == q_list[i]:
                lca = p_list[i]

        return lca.val if lca is not None else None




        