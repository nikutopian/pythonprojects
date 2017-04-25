__author__ = 'user'
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        cursum = 0
        curcount = 0
        mincurcount = 100000

        for i in range(len(nums)):
            cursum += nums[i]
            curcount += 1
            while start < len(nums) and cursum - nums[start] >= s:
                cursum -= nums[start]
                start += 1
                curcount -= 1
            if cursum >= s and curcount < mincurcount:
                mincurcount = curcount


        if mincurcount == 100000:
            mincurcount = 0

        return mincurcount

a = Solution()
b = a.minSubArrayLen(15, [1,2,3,4,5])
print(b)
