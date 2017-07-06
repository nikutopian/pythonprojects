class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        a = [lower - 1] + nums + [upper + 1]
        vals = []

        for i in range(1,len(a)):
            if a[i] - a[i-1] > 1:
                clower = a[i-1] + 1
                cupper = a[i] - 1
                if clower == cupper:
                    vals.append(str(clower))
                else:
                    vals.append('{0}->{1}'.format(clower, cupper))

        return vals


a = Solution()
print(a.findMissingRanges([0, 1, 3, 50, 75], 0, 99))




