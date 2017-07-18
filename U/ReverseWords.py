class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseString(self, s, start, end):
        i = start
        j = end
        while i<j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

    def reverseWords(self, s):
        wordExist = ' ' in s
        if not wordExist:
            return


        l = len(s)
        self.reverseString(s, 0, l - 1)

        spaceIndices = [i for i,c in enumerate(s) if c == ' ']

        istart = 0
        iend = 0
        i = s.index(' ')

        for spaceIndex in spaceIndices:
            iend = spaceIndex - 1
            self.reverseString(s, istart, iend)
            istart = spaceIndex + 1

        iend = l - 1
        self.reverseString(s, istart, iend)


a = Solution()
s = [c for c in "hello how are you. this is cool"]
a.reverseWords(s)
print(''.join(s))

