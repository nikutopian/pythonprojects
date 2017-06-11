class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mapping = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapping:
                return [mapping[diff], i]
            mapping[nums[i]] = i

        return None

a = Solution()
print(a.twoSum([2,7,11,15], 9))

