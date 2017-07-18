class Solution(object):

    def internal_remove(self, s, lasti, lastj, symbols, ans):
        ctr = 0
        for i in range(lasti, len(s)):
            if s[i] == symbols[0]:
                ctr += 1
            if s[i] == symbols[1]:
                ctr -= 1
            if ctr >= 0:
                continue
            for j in range(lastj, i+1):
                if s[j] == symbols[1] and (j == lastj or s[j-1] != symbols[1]):
                    self.internal_remove(s[:j] + s[j+1:], i, j, symbols, ans)
            return

        revs = s[::-1]

        if symbols[0] == '(':
            self.internal_remove(revs, 0, 0, [symbols[1], symbols[0]], ans)
        else:
            ans.append(revs)

    def removeInvalidParentheses(self, s):
        ans = []
        self.internal_remove(s, 0, 0, ['(', ')'], ans)
        return ans





    def removeInvalidParenthesesBFS(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0

        level = [s]

        while True:
            valid = list(filter(isvalid, level))
            if len(valid) > 0:
                return list(set(valid))
            level = [s[:i] + s[i+1:] for s in level for i in range(len(s))]

a = Solution()
print(a.removeInvalidParentheses("()())()"))


