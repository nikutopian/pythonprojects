__author__ = 'user'

import operator
import sys


def compare_building_height(a, b):
    return a > b

def compare_building_right(a, b):
    return a[1] < b[1]

class Heap:
    def __init__(self, compare_func):
        self.arr = []
        self.count = 0
        self.compare_func = compare_func

    # def compare(self, parent, child):
    #     if self.isminheap:
    #         return parent < child
    #     else:
    #         return parent > child

    def insert(self, val):
        self.arr.append(val)
        self.count = len(self.arr)
        self.heapify_from_bottom(self.count - 1)

    def adjust_node(self, pindex):
        minindex = childindex1 = pindex * 2 + 1
        childindex2 = childindex1 + 1
        if self.count <= childindex1:
            return -1

        if self.count > (childindex2) and not self.compare_func(self.arr[childindex1], self.arr[childindex2]):
            minindex = childindex2
        if not self.compare_func(self.arr[pindex], self.arr[minindex]):
            self.arr[pindex],self.arr[minindex] = self.arr[minindex],self.arr[pindex]
            return minindex
        return -1

    def heapify_from_bottom(self, index):
        pindex = (index - 1) // 2
        if pindex >= 0 and index != pindex and not self.compare_func(self.arr[pindex], self.arr[index]):
            childminindex = self.adjust_node(pindex)
            if childminindex != -1:
                self.heapify_from_bottom(pindex)

    def heapify_from_top(self, index):
        childminindex = self.adjust_node(index)
        if childminindex  != -1:
            self.heapify_from_top(childminindex)


    def peek(self):
        if self.count > 0:
            return self.arr[0]
        return None

    def top(self):
        val = self.peek()
        if val is not None:
            self.removeAtIndex(0)

        return val

    def remove(self, val):
        index = self.arr.index(val)
        if index > -1:
            self.removeAtIndex(index)

    def removeAtIndex(self, index):
        self.arr[index] = self.arr[-1]
        del self.arr[-1]
        self.count -= 1
        self.heapify_from_top(index)


class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        def right_loop(l):
            while (True):
                right = right_heap.peek()
                if right is None or right[1] >= l:
                    break
                right = right_heap.top()
                _,rr,rh = right
                height_heap.remove(rh)
                max_height = height_heap.peek()
                max_height = max_height if max_height is not None else 0
                if max_height < rh:
                    if len(skyline) > 0 and skyline[-1][0] == rr:
                        del skyline[-1]
                    skyline.append([rr,max_height])


        height_heap = Heap(compare_building_height)
        skyline = []
        right_heap = Heap(compare_building_right)
        for building in buildings:
            l,r,h = building
            right_loop(l)

            max_height = height_heap.peek()
            max_height = max_height if max_height is not None else 0

            if h > max_height:
                if len(skyline) > 0 and skyline[-1][0] == l:
                    del skyline[-1]
                skyline.append([l,h])

            height_heap.insert(h)
            right_heap.insert(building)

        right_loop(sys.maxsize)

        return skyline

        # leftxypoints = [(x1,y) for x1,x2,y in buildings]
        # rightxypoints = [(x2,y) for x1,x2,y in buildings]
        #
        # height_heap = Heap(compare_building_height)
        # right_heap = Heap(compare_building_right)
        #
        # skyline = []
        #
        # for building in buildings:
        #     x,y,h = building
        #
        #     while (True):
        #         current_right = right_heap.peek()
        #         if current_right is None or current_right[1] > x:
        #             break
        #         current_right = right_heap.top()
        #
        #     current_height = height_heap.peek()
        #
        #     height_heap.insert(building)
        #
        #     if current_height is None or h > current_height:
        #         skyline.append([x,h])










a = Solution()
print(a.getSkyline([[1,2,1],[1,2,2],[1,2,3]]))
print(a.getSkyline([[0,2147483647,2147483647]]))
print(a.getSkyline([[0,2,3],[2,5,3]]))
print(a.getSkyline([[1,10,3], [5,6,4]]))
print(a.getSkyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]))


# b = Heap(False)
# import random
# for i in range(20):
#     b.insert(random.randint(0,100))
# while b.peek() is not None:
#     print(b.top())
