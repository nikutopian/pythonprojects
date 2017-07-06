# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        headNewNode = None
        prevNewNode = None

        position_map = {}
        index = 0
        node_list = []

        cur = head

        while cur is not None:

            position_map[cur] = index
            index += 1

            curNewNode = RandomListNode(cur.label)

            node_list.append(curNewNode)

            if prevNewNode is not None:
                prevNewNode.next = curNewNode
            else:
                headNewNode = curNewNode
            prevNewNode = curNewNode

            cur = cur.next

        curNewNode = headNewNode
        cur = head

        while cur is not None and curNewNode is not None:
            if cur.random is not None:
                pos = position_map[cur.random]
                curNewNode.random = node_list[pos]

            cur = cur.next
            curNewNode = curNewNode.next




        # node_map = {}
        # for item in items:
        #     curNewNode = RandomListNode(item[0])
        #     node_map[item] = curNewNode
        #
        #
        # curNewNode = headNewNode
        # for item in items:
        #     curNewNode.random = node_map[item[1]]
        #     curNewNode = curNewNode.next

        return headNewNode





