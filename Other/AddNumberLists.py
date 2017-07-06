# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1,l2
        carry = 0
        head = tail = None

        while p1 is not None or p2 is not None:
            v = (p1.val if p1 is not None else 0) + (p2.val if p2 is not None else 0)
            v += carry
            if v >= 10:
                carry = 1
                v = v % 10
            else:
                carry = 0

            node = ListNode(v)
            if tail is None:
                head = tail = node
            else:
                tail.next = node
                tail = node

            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None

        if carry == 1:
            node = ListNode(1)
            tail.next = node
            tail = node

        return head





def convertToListNode(num):
    head = None
    tail = None
    while num > 0:
        d = num % 10
        num = num // 10
        node = ListNode(d)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head



def printList(l):
    mylist = []
    while l is not None:
        mylist.insert(0, l.val)
        l = l.next
    print (mylist)

printList(convertToListNode(2315))

a  = Solution()
printList(a.addTwoNumbers(convertToListNode(5), convertToListNode(5)))
printList(a.addTwoNumbers(convertToListNode(2315), convertToListNode(412)))
printList(a.addTwoNumbers(convertToListNode(2919), convertToListNode(412)))
