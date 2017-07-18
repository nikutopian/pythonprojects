class Solution(object):
    def recursive_wordbreak(self, s, wordDict, wordmap):
        if s in wordmap:
            return wordmap[s]

        res = []
        if len(s) == 0:
            res.append("")
            return res

        for word in wordDict:
            if s.startswith(word):
                sublist = self.recursive_wordbreak(s[len(word):], wordDict, wordmap)

                for sub in sublist:
                    wordsub = word
                    if len(sub) > 0:
                        wordsub += " " + sub
                    res.append(wordsub)

        wordmap[s] = res
        return res


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordmap = {}

        return self.recursive_wordbreak(s, wordDict, wordmap)






a = Solution()
print(a.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))










