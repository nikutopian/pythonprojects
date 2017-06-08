class TrieNode:
    def __init__(self):
        self.isleaf = False
        self.children = {}
    def insert(self, itemlist):
        if itemlist is None or len(itemlist) <= 0:
            self.isleaf = True
            return
        c = itemlist[0]
        if not c in self.children:
            self.children[c] = TrieNode()
        self.children[c].insert(itemlist[1:])

    def exists(self, itemlist):
        if itemlist is None or len(itemlist) <= 0:
            return self.isleaf
        c = itemlist[0]
        if not c in self.children:
            return False
        return self.children[c].exists(itemlist[1:])

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, itemlist):
        self.head.insert(itemlist)

    def exists(self, itemlist):
        return self.head.exists(itemlist)

class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordSet = set(wordDict)

        done = [False] * len(s)

        for i in range(0, len(s)):
            if not done[i] and \
                s[:i+1] in wordSet:
                done[i] = True
            if done[i] == True:
                if i == len(s) - 1:
                    return True
                for j in range(i+1, len(s)):
                    if not done[j] and \
                        s[i+1:j+1] in wordSet:
                        done[j] = True
                    if done[j] and \
                        j == len(s) - 1:
                        return True

        return False





a = Solution()
print(a.wordBreak('leetcode', ['leet', 'code']))
print(a.wordBreak('leetcode', ['leet', 'cod']))
print(a.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))




