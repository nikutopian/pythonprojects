class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return []
        output = [0] * len(nums)
        leftprod = 1

        for i in range(len(nums)):
            output[i] = leftprod * nums[i]
            leftprod = output[i]

        rightprod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i-1] * rightprod if i > 0 else rightprod
            rightprod *= nums[i]

        return output

a = Solution()
print(a.productExceptSelf([0,0]))
print(a.productExceptSelf([1,2,3,4]))

