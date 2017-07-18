class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        min1 = min2 = 2 ** 32


        for num in nums:
            if num - min2 > 0:
                return True
            min2 = num if num - min1 > 0 else min2
            min1 = min(min1, num)


        return False

a = Solution()
a.increasingTriplet([1,2,3,5])
a.increasingTriplet([5,3,2])
a.increasingTriplet([1,2])
a.increasingTriplet([1,2,5])
a.increasingTriplet([2,1,0])
a.increasingTriplet([2,1,3,2,5])
