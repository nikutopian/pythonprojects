class Solution(object):
    def internalmaxProfit(self, prices, k):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = min(len(prices), k)
        releases = [0] * k
        holds = [-1 * (2 ** 32 - 1)] * k
        soldsofar = 0
        maxp = 0

        for p in prices:
            for i in range(min(soldsofar + 1, k-1),-1,-1):
                releases[i] = max(releases[i], holds[i] + p)
                maxp = max(releases[i], maxp)
                holds[i] = max(holds[i], releases[i-1] - p if i > 0 else -p)
                soldsofar += 1

                # if releases[i] > 0:
                #     soldsofar = i + 2

        print(holds)
        print(releases)
        return maxp



    def maxProfit(self, prices, k=6):
        """
        :type prices: List[int]
        :rtype: int
        """

        return self.internalmaxProfit(prices, k)

a = Solution()
# print(a.maxProfit([6,1,3,2,4,7]))
print(a.maxProfit([1,2,4,2,5,7,2,4,9,0,9]))
print(a.maxProfit([8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]))
# print(a.maxProfit([7, 1, 5, 3, 6, 4, 8, 5, 10]))
# print(a.maxProfit([7, 1, 6, 3, 5, 4]))
# print(a.maxProfit([7, 6, 5, 4]))
# print(a.maxProfit([3,2,6,5,0,3]))

