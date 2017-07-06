class TreeNode:
    def __init__(self, x):
        self.val = x
        self.cnt = 0

    def search(self, x):
        if x == self.val:
            return self.cnt
        if x < self.val:
            return

class BST:
    def __init__(self):
        self.head = None

    def insert(self, x):
        if self.head == None:
            self.head = TreeNode(x)

    def search(self, x):
        if self.head == None:
            return 0

class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.arr = [0] * (n + 1)

    def update(self, index, val):
        while index > 0:
            self.arr[index] += val
            index -= index & -index

        # print(self.arr)

    def search(self, index):
        sum = 0
        if index >= self.n:
            return sum
        while index < self.n:
            sum += self.arr[index]
            index += index & -index
        return sum

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        snums = sorted(nums)
        b = BIT(len(snums))

        res = 0

        def findindex(mynums, val):
            l = 0
            r = len(mynums) - 1

            while(l <= r):
                m = l + ((r - l) >> 1)
                if mynums[m] >= val:
                    r = m -1
                else:
                    l = m + 1

            return l + 1

        # print(nums)
        # print(snums)
        # rs = []
        # iis = []
        # js = []

        for item in nums:
            i = findindex(snums, item * 2 + 1)
            # iis.append(i)
            r = b.search(i)
            # rs.append(r)
            if r is not None:
                res += r
            j = findindex(snums, item)
            # js.append(j)
            b.update(j, 1)

        # print(js)
        # print(iis)
        # print(rs)


        return res


a = Solution()
print(a.reversePairs([2 , 5 , 8 , 10 , 3 , 5 , 1 , 9 , 4]))

print(a.reversePairs([1,5,12,-3,2,5,34,3,4,45,6,7,12]))

