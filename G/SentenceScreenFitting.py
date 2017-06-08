class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """

        i = 0

        ls = [len(word) for word in sentence]
        totallen = sum(ls) + (len(ls))

        index = 0
        completions = 0
        rowsdone = False

        while (i < rows):
            j = -1

            # if not rowsdone and i > 0 and index == 0:
            #     r = i
            #     completions *= (rows // r)
            #     i = rows % r
            #     rowsdone = True
            #

            while (j + ls[index] + 1 <= cols):
                if index == 0 and cols >= totallen - 1:
                    currentcompletions = (cols - j) // totallen
                    completions += currentcompletions
                    j += currentcompletions * totallen

                if j + ls[index] + 1 <= cols:
                    j += ls[index] + 1
                    index += 1

                    if index == len(ls):
                        index = 0
                        completions += 1

            i += 1


        return completions


a = Solution()
print(a.wordsTyping(["a", "bcd", "e"], 3, 6))
print(a.wordsTyping(["hello", "world"], 2, 8))
print(a.wordsTyping(["I", "had", "apple", "pie"], 4, 5))

print(a.wordsTyping(["a", "bcd", "e"], 3, 13))

print(a.wordsTyping(["try","to","be","better"], 10000, 9001))


print(a.wordsTyping(["abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r","abcdef","ghijkl","mnop","qrs","tuv","wxyz","asdf","ogfd","df","r"], 19999, 19995))

