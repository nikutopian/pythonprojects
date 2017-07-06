class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            elif nums[mid] == 2:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1

        print(nums)

a = Solution()
a.sortColors([1])
a.sortColors([0])
a.sortColors([2])
a.sortColors([1,0])
a.sortColors([2,0])
a.sortColors([2,1,0])
a.sortColors([2,1,2,0,0,0,1,2,2,1,1,0])
