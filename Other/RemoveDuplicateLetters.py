__author__ = 'user'
import operator


# class Solution(object):
#     def removeDuplicateLetters(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         charmap = {}
#
#         for i in range(len(s)):
#             charmap[s[i]] = i
#
#         scharmap = sorted(charmap.items(), key=operator.itemgetter(1))
#
#         sindex = 0
#
#         outputs = []
#         donechars = set()
#
#
#         for c,i in scharmap:
#             curchar = c
#             minchar = c
#             for k in range(sindex, i):
#                 if s[k] not in donechars and minchar > s[k]:
#                     minchar = s[k]
#
#             if minchar not in donechars:
#                 outputs.append(minchar)
#                 donechars.add(minchar)
#             if curchar not in donechars:
#                 outputs.append(curchar)
#                 donechars.add(curchar)
#
#             sindex = i+1
#
#         return ''.join(outputs)

import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        resultSet = set()
        stack = list()
        for c in s:
            counter[c] -= 1
            if c in resultSet:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                resultSet.remove(stack.pop())
            resultSet.add(c)
            stack.append(c)
            print(stack)
        return ''.join(stack)

a = Solution()
# print(a.removeDuplicateLetters('abacb'))
print(a.removeDuplicateLetters('bcabc'))
# print(a.removeDuplicateLetters('dzzbzrrzarebecrredrzrzrz'))
# print(a.removeDuplicateLetters('bcabc'))
# print(a.removeDuplicateLetters('cbacdcbc'))
# print(a.removeDuplicateLetters('cbacdcbc'))
#





