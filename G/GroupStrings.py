class Solution(object):
    def __init__(self):
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.amap = {v:k for k,v in enumerate(self.alphabets)}

    def get_char_diff(self, c1, c2):
        diff = ((self.amap[c2] - self.amap[c1]) + 26) % 26
        return str(diff)

    def get_code(self, string):
        code = []
        for i in range(0, len(string)-1):
            code.append(self.get_char_diff(string[i+1], string[i]))
        return ",".join(code)

    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        mymap = {}

        for string in strings:
            code = self.get_code(string)
            if code not in mymap:
                mymap[code] = []
            mymap[code].append(string)

        return [v for k,v in mymap.items()]

a = Solution()
print(a.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

