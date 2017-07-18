class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nummap = {}
        maxlen = 0
        for i,num in enumerate(nums):
            if num in nummap:
                continue

            left = nummap[num - 1] if num - 1 in nummap else 0
            right = nummap[num + 1] if num + 1 in nummap else 0
            nummap[num] = left + right + 1
            maxlen = max(maxlen, nummap[num])

            nummap[num - left] = nummap[num]
            nummap[num + right] = nummap[num]

        return maxlen

a = Solution()
print(a.longestConsecutive([1,2,0,1]))
# print(a.longestConsecutive([100, 4, 200, 1, 101, 2, 87, 6, 12, 3, 132, 5, 102, 103, 104, 105, 106]))






