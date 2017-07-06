class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        num = numerator

        nummap = {}
        out = "0"

        begin = -1

        if num > denominator:
            out = "{0}".format(num // denominator)
            num = num % denominator

        index = 0
        arr = []
        while True:
            if num == 0:
                break

            nummap[num] = index

            if num < denominator:
                num *= 10
                index += 1

            while num < denominator:
                num *= 10
                index += 1
                arr.append(0)

            arr.append(num // denominator)
            num = num % denominator


            if num in nummap:
                begin = nummap[num]
                break


        if len(arr) > 0:
            out += "."

        for i, item in enumerate(arr):
            if i == begin:
                out += "("
            out += str(item)

        if begin >= 0:
            out += ")"



        print(out)

        return out



a = Solution()
a.fractionToDecimal(1,90)
a.fractionToDecimal(1,2)
a.fractionToDecimal(2,1)
a.fractionToDecimal(10,2)
a.fractionToDecimal(10,230)
a.fractionToDecimal(10,100)
a.fractionToDecimal(10,5)
# a.fractionToDecimal(1,9)
# a.fractionToDecimal(1,3)
# a.fractionToDecimal(1,6)
# a.fractionToDecimal(1,11)
# a.fractionToDecimal(1,12)
# a.fractionToDecimal(1,7)
# a.fractionToDecimal(1,14)
# a.fractionToDecimal(1,17)




