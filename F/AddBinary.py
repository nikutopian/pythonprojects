class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)

        if la < lb :
            a,b = b,a
            la,lb = lb,la

        c = 0
        rl = []

        i = la - 1
        j = lb - 1

        while i >= 0 or j >= 0:
            ba = int(a[i])
            bb = 0
            if j >= 0:
                bb = int(b[j])
            s = ba + bb + c

            if s > 1:
                s = s % 2
                c = 1
            else:
                c = 0

            rl.append(str(s))
            i -= 1
            j -= 1

        if c == 1:
            rl.append('1')


        return ''.join(rl[::-1])

a = Solution()
print(a.addBinary('01', '10'))
print(a.addBinary('01', '1000'))
print(a.addBinary('11101', '1000'))
print(a.addBinary('11', '1'))


