import sys

class Solution(object):
    def __init__(self):
        self.mem = []

    def numDecodingsInternal(self,s,index):
        if index >= len(s)-1:
            return 1

        if self.mem[index] != sys.maxsize:
            return self.mem[index]

        num = self.numDecodingsInternal(s, index+1)


        if s[index] == '1' or (s[index] == '2' and s[index+1] <= '6'):
            num += self.numDecodingsInternal(s, index+2)

        self.mem[index] = num

        return num


    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) <= 1:
            return len(s)

        self.mem = [sys.maxsize] * len(s)

        return self.numDecodingsInternal(s, 0)

        
        
a = Solution()
print(a.numDecodings(''))
print(a.numDecodings('1'))
print(a.numDecodings('1122'))