class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def generate(seq, open, close, n, result):
            if len(seq) == n * 2:
                result.append(seq)
                return
            if open < n:
                generate(seq + '(', open+1, close, n, result)
            if close < open:
                generate(seq + ')', open, close+1, n, result)

        result = []
        generate('', 0, 0, n, result)
        return result



        # def generate(seq, left, right):
        #     if right >= left >= 0:
        #         if not right:
        #             yield seq
        #         for q in generate(seq + '(', left-1,right): yield q
        #         for q in generate(seq + ')', left,right-1): yield q
        # return list(generate('', n, n))

a = Solution()
print(a.generateParenthesis(3))
print(a.generateParenthesis(8))
