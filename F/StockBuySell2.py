class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = 2 ** 32 - 1
        sump = 0

        bought = False

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                sump += (prices[i] - minprice)
                minprice = prices[i]

        return sump

a = Solution()
print(a.maxProfit([2, 1, 2, 0, 1]))
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
print(a.maxProfit([7, 1, 6, 3, 5, 4]))
print(a.maxProfit([7, 6, 5, 4]))
print(a.maxProfit([3,2,6,5,0,3]))

