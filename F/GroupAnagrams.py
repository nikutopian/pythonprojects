class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strmap = {}

        for str in strs:
            sstr = ''.join(sorted(str))
            if sstr not in strmap:
                strmap[sstr] = []
            strmap[sstr].append(str)

        return strmap.values()

a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

