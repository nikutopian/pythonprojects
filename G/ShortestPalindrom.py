class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        arr = []

        while i < j:
            if s[i] != s[j]:
                arr.append(s[j])
            else:
                i += 1
            j -= 1

        return ''.join(arr) + s

a = Solution()
print(a.shortestPalindrome("aacecaaa"))
print(a.shortestPalindrome("abcd"))
print(a.shortestPalindrome("aabba"))

