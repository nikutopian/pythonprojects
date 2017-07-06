# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serializeinternal(self, node, l, index):
        if node is None:
            return
        l.append((index, node.val))
        self.serializeinternal(node.left, l, index * 2 + 1)
        self.serializeinternal(node.right, l, index * 2 + 2)


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        self.serializeinternal(root, l, 0)
        return '|'.join(['{0},{1}'.format(i[0], i[1]) for i in l])



    def deserializeinternal(self, m, index):
        if index not in m:
            return None
        node = TreeNode(m[index])
        node.left = self.deserializeinternal(m, index * 2 + 1)
        node.right = self.deserializeinternal(m, index * 2 + 2)
        return node



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = [item.split(',') for item in data.split('|')]
        if any(len(item) != 2 for item in l):
            return None
        m = {}

        for index,val in l:
            i = int(index)
            v = int(val)
            m[i] = v

        return self.deserializeinternal(m, 0)






# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

codec = Codec()
node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node0.left = node1
node0.right = node2
node2.left = node3
node2.right = node4
node4.left = node5

s = codec.serialize(node0)
print(s)
node0 = None

rnode = codec.deserialize(s)
print(codec.serialize(rnode))
hey = codec.deserialize('')



