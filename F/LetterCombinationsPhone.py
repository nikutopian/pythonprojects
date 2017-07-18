class Solution(object):
    def letterCombo(self, wordsofar, letterslist, index):
        if len(letterslist) <= index:
            yield wordsofar
        else:

            for letter in letterslist[index]:
                for word in self.letterCombo(wordsofar + letter, letterslist, index + 1):
                    yield word

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = \
            {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'
             }

        letterslist = [mapping[digit] for digit in digits]

        words = list(self.letterCombo('', letterslist, 0))

        words = [word for word in words if word != '']

        return words

a = Solution()
print(a.letterCombinations(''))
print(a.letterCombinations('23'))
print(a.letterCombinations('4592'))



