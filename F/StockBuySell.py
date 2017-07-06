class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > maxp:
        #             maxp = prices[j] - prices[i]

        minprice = 2 ** 32 - 1
        maxp = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            if maxp < prices[i] - minprice:
                maxp = prices[i] - minprice




        return maxp

a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
print(a.maxProfit([7, 1, 6, 3, 5, 4]))
print(a.maxProfit([7, 6, 5, 4]))
print(a.maxProfit([3,2,6,5,0,3]))

