# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def next(self, p):
        return p.next if p is not None else None

    def detectCycle(self, A):
        p1 = self.next(A)
        p2 = self.next(self.next(A))
        while p1 != p2:
            p1 = self.next(p1)
            p2 = self.next(self.next(p2))

        if p1 is not None and p2 is not None and p1 == p2:

            p1 = A

            while p1 != p2:
                p1 = self.next(p1)
                p2 = self.next(p2)

            return p1

        return None




a = Solution()
def getlist(arr):
    headnode = prevnode = None
    for item in arr:
        curnode = ListNode(item)
        if headnode is None:
            headnode = curnode
        else:
            prevnode.next = curnode
        prevnode = curnode
    return headnode

b = getlist([1,2,3,4,5,6,7])
b.next.next.next.next.next.next.next = b.next.next.next.next

res = a.detectCycle(b)
print(res.val)


