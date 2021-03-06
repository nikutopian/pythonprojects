
from collections import deque


class Solution:
    def getAdjacencyMatrix(self, wordList):
        l = len(wordList)
        adj = [[False] * l for i in range(l)]
        for i in range(l):
            for j in range(i, l):
                if self.isOneCharEdit(wordList[i], wordList[j]):
                    adj[i][j] = True
                    adj[j][i] = True

        return adj

    def isOneCharEdit(self, beginWord, endWord):
        if len(beginWord) != len(endWord):
            return False
        count = 0
        for c,d in zip(beginWord, endWord):
            if c != d:
                count += 1
            if count > 1:
                return False
        if count == 1:
            return True
        return False

    def bfs(self, adj, s, e):
        q = deque()
        q.append((s,0))

        visited = set()

        while len(q) > 0:
            (c,index) = q.popleft()

            if c == e:
                return (index + 1)

            visited.add(c)
            adjvectors = [i for i in range(len(adj)) if adj[c][i] and i not in visited]
            for v in adjvectors:
                q.append((v, index+1))

        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList = [beginWord] + wordList

        adj = self.getAdjacencyMatrix(wordList)
        return self.bfs(adj, wordList.index(beginWord), wordList.index(endWord))



    def findOneCharEditWords(self, beginWord, wordList):
        outList = []
        for word in wordList:
            if self.isOneCharEdit(beginWord, word):
                outList.append(word)
        return outList

    def findLaddersInternal(self, beginWord, endWord, wordList, excludeWordList):

        outList = []

        if beginWord == endWord:
            outList.append([endWord])
            return outList

        minLength = 1000000

        nextWords = self.findOneCharEditWords(beginWord, wordList)


        for nextWord in nextWords:
            if nextWord in excludeWordList:
                continue
            newPaths = self.findLaddersInternal(nextWord, endWord, wordList, excludeWordList + [nextWord])
            if len(newPaths) > 0:
                if len(newPaths[0]) <= minLength:
                    if len(newPaths[0]) < minLength:
                        outList = []
                    for newPath in newPaths:
                        outList.append([beginWord] + newPath)
                    minLength = len(newPaths[0])

        return outList

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        a = []
        return self.findLaddersInternal(beginWord, endWord, wordList, a)

a = Solution()
# b = a.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
# print(b)
# c = a.findLadders("qa",
# "sq",
# ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
# print(c)

b = a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])

print(b)
b = a.ladderLength("hit", "cog", ["hot","cog","dot","dog","hit","lot","log"])
print(b)