__author__ = 'user'

class Solution(object):
    def nearestNumber(self, num):
        return num - 1 if num > 0 else 1

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """

        l = len(n)
        out = list(n)

        tens = 1
        diff = 0
        for i,j in zip(range(0,l//2), range(l-1,(l-1)//2,-1)):
            ci = int(n[i])
            cj = int(n[j])
            altdiff = currdiff = (ci - cj) * tens
            if j-i == 1:
                altdiff = ((ci + 1 - cj) * tens) + (10 * tens)

            if abs(altdiff) < abs(currdiff):
                out[i] = str(ci + 1)
                out[j] = str(ci + 1)
                currdiff = altdiff
            else:
                out[j] = str(ci)

            diff += currdiff
            tens *= 10

        diff = abs(diff)

        if diff == 0:
            mid = (l - 1) // 2
            midnext = l // 2
            oldnum = int(n[mid])
            oldnumnext = int(n[midnext])
            newnum = self.nearestNumber(oldnum)
            out[mid] = out[midnext] = str(newnum)
            diff = (10 ** mid) * abs(newnum - oldnum)
            if midnext != mid:
                diff += (10 ** midnext) * abs(newnum - oldnumnext)


        if l > 1 and n[0] == "1":
            newdiff = 0
            tens = 1
            for i in range(l-1,0,-1):
                ci = int(n[i])
                if i == l-1:
                    ci += 1

                newdiff += ci * tens
                tens *= 10

            if newdiff <= diff:
                out = ['9'] * (l-1)
            # print('newdiff = {0}'.format(newdiff))

        if l > 1 and n[0] == '9':
            newdiff = 0
            tens = 1
            for i in range(l-1,0,-1):
                ci = 9 - int(n[i])
                if i == l-1:
                    ci += 2

                newdiff += ci * tens
                tens *= 10

            # print('newdiff = {0}'.format(newdiff))
            if newdiff < diff:
                out = ['1'] + ['0'] * (l-1) + ['1']




        ret = "".join(out)
        # print('diff = {0}'.format(diff))


        return ret

a = Solution()
print(a.nearestPalindromic("1"))
print(a.nearestPalindromic("3"))
print(a.nearestPalindromic("101"))
print(a.nearestPalindromic("11"))
print(a.nearestPalindromic("9"))
print(a.nearestPalindromic("1283"))
# print(a.nearestPalindromic("99"))
# print(a.nearestPalindromic("999"))
# print(a.nearestPalindromic("100"))
# print(a.nearestPalindromic("202"))
# print(a.nearestPalindromic("2002"))
# b = a.nearestPalindromic("523")
# print(b)
