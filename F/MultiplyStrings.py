class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        digits1 = [int(c) for c in num1]
        digits2 = [int(c) for c in num2]



        output = []

        offset = -1

        for i in range(len(num1) - 1, -1, -1):
            offset += 1
            for j in range(len(num2) - 1, -1, -1):
                carry = digits1[i] * digits2[j]

                off = offset + (len(num2) - 1 - j) - 1

                while True:
                    off += 1
                    if len(output) > off:
                        carry = output[off] + carry
                    else:
                        output.append(0)

                    dig = carry % 10
                    carry = carry // 10

                    output[off] = dig

                    if carry <= 0:
                        break

        # if carry > 0:
        #     output.append(carry)

        while len(output) > 0 and output[-1] == 0:
            output.pop()
        if len(output) == 0:
            output.append(0)

        return ''.join([str(i) for i in output[::-1]])



a = Solution()
print(a.multiply('98', '0'))
print(a.multiply('98', '1'))
print(a.multiply('98', '2'))
print(a.multiply('2', '98'))

print(a.multiply('98', '9'))
print(a.multiply('123', '100'))
print(a.multiply('8745123', '1312'))
