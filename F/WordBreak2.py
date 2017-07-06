class Solution(object):
    def getpath(self, prev, index):
        print(index)
        if index == 0:
            return []
        if len(prev[index]) > 0:
            paths = [self.getpath(prev, pindex) for pindex in prev[index]]
            print(paths)
            paths = [path + [index] for path in paths if path is not None]
            return paths
        return None


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset = set(wordDict)

        maxlen = max([len(word) for word in wordDict])
        prev = [[] for _ in range(len(s))]

        for i in range(len(s)):
            if s[:i+1] in wordset:
                prev[i].append(0)

            j = i+1
            count = 0
            while j < len(s):
                if s[i+1:j+1] in wordset:
                    prev[j].append(i)
                j += 1

        print(prev)

        paths = self.getpath(prev, len(s) - 1)

        print(paths)






a = Solution()
a.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])










