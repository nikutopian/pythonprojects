
class Solution(object):

    def ispalindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        mymap = {}
        output = []

        for i,word in enumerate(words):
            mymap[word] = i

        for i,word in enumerate(words):
            if len(word) == 0:
                for k,word2 in enumerate(words):
                    if word != word2:
                        output.append([i,k])

            for j in range(len(word)):
                sub1 = word[:j]
                sub2 = word[j:]
                revsub1 = sub1[::-1]
                revsub2 = sub2[::-1]

                if self.ispalindrome(sub1) and revsub2 in mymap and revsub2 != word:
                    output.append([mymap[revsub2], i])
                if self.ispalindrome(sub2) and revsub1 in mymap and revsub1 != word:
                    output.append([i, mymap[revsub1]])

        return output


a = Solution()
print(a.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))
print(a.palindromePairs(["bat", "tab", "cat"]))
print(a.palindromePairs(["a",""]))







