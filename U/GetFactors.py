class Solution(object):


    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def factor(n, i, factorssofar, result):
            while i * i <= n:
                if n % i == 0:
                    result += [factorssofar + [i, n//i]]
                    factor(n//i, i, factorssofar + [i], result)
                i += 1

            return result

        return factor(n, 2, [], [])

a = Solution()
print(a.getFactors(100))



