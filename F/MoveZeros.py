class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zeroindex = 0
        zerocount = 0
        while zeroindex < length:
            while zeroindex < length and nums[zeroindex] == 0:
                zeroindex += 1
                zerocount += 1
            if zeroindex < length and zerocount > 0:
                i = zeroindex - zerocount
                nums[zeroindex], nums[i] = nums[i], nums[zeroindex]

            zeroindex += 1


        return nums
        

a = Solution()
print(a.moveZeroes([0, 1, 0, 3, 12]))
print(a.moveZeroes([]))
print(a.moveZeroes([0]))
print(a.moveZeroes([1]))
print(a.moveZeroes([0, 1]))
print(a.moveZeroes([1, 0]))
print(a.moveZeroes([0, 0, 0]))
print(a.moveZeroes([1, 1, 1]))
print(a.moveZeroes([0, 1, 0, 3, 12, 0, 0, 5, 8, 9, 12, 0]))



