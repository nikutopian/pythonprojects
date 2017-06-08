class Solution(object):
    def internal(self, s, sofar):
        if len(s) == 0:
            if sofar == 0:
                return True, ""
            else:
                return False, None


        nextsofar = sofar
        wo, wor = self.internal(s[1:], nextsofar)
        if s[0] == '(':
            nextsofar += 1
        elif s[0] == ')':
            nextsofar -= 1

        if nextsofar >= 0:
            w, wr = self.internal(s[1:], nextsofar)

        output = wor



    def internal_removeInvalid(self, s, i, j, mat):
        length = len(s)
        if i < 0:
            return None

        if i >= length or j >= length:
            return None

        if j == length - 1:
            if i == 0:
                mat[i][j] = [[]]
                return [[]]
            else:
                return None

        if mat[i][j] is not None:
            return mat[i][j]
        xi = i
        if s[j] == '(':
            xi += 1
        elif s[j] == ')':
            xi -= 1

        wo = self.internal_removeInvalid(s, xi, j + 1, mat)

        if xi != i:
            w = self.internal_removeInvalid(s, i, j + 1, mat)
            if w is not None:
                w = [[j] + x for x in w]

        if w is not None and wo is not None:
            if len(wo[0]) == len(w[0]):
                wo += w
            elif len(wo[0]) > len(w[0]):
                wo = w
        elif w is not None:
            wo = w



        mat[i][j] = wo

        return wo


    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        length = len(s)
        mat = [[None] * length for _ in range(length)]


        retval = self.internal_removeInvalid(s, 0, 0, mat)

        return retval

a = Solution()
print(a.removeInvalidParentheses("()())()"))


