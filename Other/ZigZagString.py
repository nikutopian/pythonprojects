class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        diffs = [(numRows * 2 - 2), 0]
        stringlist = []
        for i in range(numRows):
            k = i
            index = 0
            rowlist = []
            while k < len(s):
                inc = diffs[index]
                index = 1 - index
                if inc > 0:
                    rowlist.append(s[k])
                    k += inc

            diffs = [diffs[0] - 2, diffs[1] + 2]
            stringlist.append(''.join(rowlist))

        return ''.join(stringlist)

a = Solution()
print(a.convert("A", 1))
print(a.convert("PAYPALISHIRING", 3))