class Solution(object):
    def internalmaxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        release1 = release2 = 0
        hold1 = hold2 = -1 * (2 ** 32 - 1)

        for p in prices:
            release2 = max(release2, hold2 + p)
            hold2 = max(hold2, release1 - p)
            release1 = max(release1, hold1 + p)
            hold1 = max(hold1, -p)


        return release2



    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        return self.internalmaxProfit(prices)


a = Solution()
print(a.maxProfit([6,1,3,2,4,7]))
print(a.maxProfit([2, 1, 2, 0, 1]))
print(a.maxProfit([7, 1, 5, 3, 6, 4, 8, 5, 10]))
print(a.maxProfit([7, 1, 6, 3, 5, 4]))
print(a.maxProfit([7, 6, 5, 4]))
print(a.maxProfit([3,2,6,5,0,3]))

