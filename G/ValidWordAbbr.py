from collections import Counter
class ValidWordAbbr(object):

    def __get_abbr(self, word):
        abbr = word
        if len(word) >= 3:
            abbr = '{0}{1}{2}'.format(word[0], len(word), word[-1])

        return abbr


    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """


        self.mapping = Counter()

        self.mapset = set(dictionary)

        # self.mapping = Counter()
        for word in dictionary:
            abbr = self.__get_abbr(word)
            if abbr != word:
                self.mapping[abbr] += 1



    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = self.__get_abbr(word)
        return (len(word) < 3 and word in self.mapset) or \
                (word in self.mapset and self.mapping[abbr] == 1) or \
                (word not in self.mapset and abbr not in self.mapping)

        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

l = [ "deer", "door", "cake", "card", "care", "wh", "blah", "weh" ]
a = ValidWordAbbr(l)
print([a.isUnique(i) for i in l])

b = ValidWordAbbr(["deer","door","cake","card"])
print(([b.isUnique(i) for i in ["dear", "cart", "cane","make"]]))
