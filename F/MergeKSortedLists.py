# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Heap:
    def __init__(self, capacity, compfunc):
        self.arr = [-1] * capacity
        self.count = 0
        self.compfunc = compfunc

    def insert(self, val):
        if self.count == len(self.arr):
            return False
        self.arr[self.count] = val
        self.count += 1
        self.heapify_from_bottom(self.count - 1)

        return True

    def size(self):
        return self.count

    def peek_top(self):
        if self.count > 0:
            return self.arr[0]
        return None

    def extract_top(self):
        top_val = self.peek_top()
        if top_val is None:
            return None
        self.count -= 1
        if self.count > 0:
            self.arr[0] = self.arr[self.count]
            self.heapify(0)

        return top_val

    def heapify(self, index):
        leftindex = index * 2 + 1
        rightindex = index * 2 + 2
        minindex = index
        if leftindex < self.count and self.compfunc(self.arr[minindex], self.arr[leftindex]):
            minindex = leftindex
        if rightindex < self.count and self.compfunc(self.arr[minindex], self.arr[rightindex]):
            minindex = rightindex

        if minindex != index:
            self.arr[index], self.arr[minindex] = self.arr[minindex], self.arr[index]
            self.heapify(minindex)

        return

    def heapify_from_bottom(self, index):
        parentindex = (index - 1) // 2
        if parentindex >= 0 and self.compfunc(self.arr[parentindex], self.arr[index]):
            self.arr[parentindex], self.arr[index] = self.arr[index], self.arr[parentindex]
            self.heapify_from_bottom(parentindex)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        heap = Heap(len(lists), lambda x,y: x.val > y.val)

        for list1 in lists:
            if list1 is not None:
                heap.insert(list1)

        newlist = None
        prevlistnode = None

        while heap.size() > 0:
            topnode = heap.extract_top()
            newlistnode = ListNode(topnode.val)
            if newlist is None:
                newlist = prevlistnode = newlistnode
            else:
                prevlistnode.next = newlistnode
                prevlistnode = newlistnode
            if topnode.next is not None:
                heap.insert(topnode.next)

        return newlist

def getListNodeList(arr):
    headnode = None
    prevnode = None
    for item in arr:
        curnode = ListNode(item)
        if headnode is not None:
            prevnode.next = curnode
        else:
            headnode = curnode
        prevnode = curnode

    return headnode

def getsimplearray(listnode):
    arr = []
    while listnode is not None:
        arr.append(listnode.val)
        listnode = listnode.next
    return arr


a = Solution()
# out = a.mergeKLists([getListNodeList([1,2,3, 10, 12, 17]), getListNodeList([4,8,9,10,12]), getListNodeList([102,103]), getListNodeList([-2,0,45,56])])
# print(getsimplearray(out))

# inp = [[-4],[-10,-6,-6],[0,3],[2],[-10,-9,-8,3,4,4],[-10,-10,-8,-6,-4,-3,1],[2],[-9,-4,-2,4,4],[-4,0]]
inp = [[1],[0]]
inp1 = [getListNodeList(item) for item in inp]
print(getsimplearray(a.mergeKLists(inp1)))
