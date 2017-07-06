class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {}

        curlength = 0
        maxlength = 0
        previ = 0

        for i,c in enumerate(s):
            if c not in mapping:
                curlength += 1
            else:
                previ = max(mapping[c], previ)
                curlength = i - previ

            mapping[c] = i
            maxlength = max(maxlength, curlength)



        return maxlength

a = Solution()
print(a.lengthOfLongestSubstring('abcabcbb'))
print(a.lengthOfLongestSubstring('abxbcxdxbdabxbcxdxbd'))
print(a.lengthOfLongestSubstring('bbb'))
print(a.lengthOfLongestSubstring('pwwkew'))
print(a.lengthOfLongestSubstring('tmmzuxt'))
print(a.lengthOfLongestSubstring('a'))