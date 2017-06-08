class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        outoutstr = []

        index = 0
        for c in S[::-1]:

            if c != '-':
                index += 1
                outoutstr.append(c.upper())
                if index % (K) == 0:
                    outoutstr.append('-')
        if len(outoutstr) > 0 and outoutstr[-1] == '-':
            outoutstr.pop()

        return ''.join(outoutstr[::-1])


a = Solution()
print(a.licenseKeyFormatting("2-4A0r7-4k", 3))
print(a.licenseKeyFormatting("2-4A0r7-4k", 4))
print(a.licenseKeyFormatting("2-4A0r7-4k", 1))
print(a.licenseKeyFormatting("2-4A0r7-4k", 12))
print(a.licenseKeyFormatting("abc-abc", 3))
print(a.licenseKeyFormatting("---", 3))


