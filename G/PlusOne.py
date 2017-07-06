class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        outdigits = digits[:]

        i = len(outdigits) - 1

        while i >= 0 and outdigits[i] == 9:
            outdigits[i] = 0
            i -= 1

        if i >= 0:
            outdigits[i] += 1
        else:
            outdigits.insert(0, 1)

        return outdigits

a = Solution()
print(a.plusOne([int(c) for c in '12345']))
print(a.plusOne([int(c) for c in '123499']))
print(a.plusOne([int(c) for c in '10']))
print(a.plusOne([int(c) for c in '1']))
print(a.plusOne([int(c) for c in '9']))
print(a.plusOne([int(c) for c in '99']))



