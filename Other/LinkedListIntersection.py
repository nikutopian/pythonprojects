# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getLength(self, head):
        l = 0
        p = head
        while p is not None:
            p = p.next
            l += 1
        return l

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = self.getLength(headA)
        l2 = self.getLength(headB)
        p1 = headA
        p2 = headB
        print(l1)
        print(l2)

        if l1 > l2:
            for i in range(l1 - l2):
                p1 = p1.next
        if l2 > l1:
            for i in range(l2 - l1):
                p2 = p2.next

        while p1 is not None and p2 is not None:
            if p1.val == p2.val:
                return p1
            p1 = p1.next
            p2 = p2.next

        return None

def getlistnode(arr):
    headnode = None
    prevnode = None
    for item in arr:
        curnode = ListNode(item)
        if headnode is None:
            headnode = curnode
        else:
            prevnode.next = curnode
        prevnode = curnode
    return headnode

a = Solution()
print(a.getIntersectionNode(getlistnode([]), getlistnode([])))
print(a.getIntersectionNode(getlistnode([0,1,2,3]), getlistnode([1,2,3])))


        