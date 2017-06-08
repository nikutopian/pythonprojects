class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        map = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }

        specials = [map[100], map[1000], map[1000000], map[1000000000]]

        cur = num
        l = []

        pos = 0
        index = 0
        prevdigit = 0

        if num == 0:
            return map[num]

        def put_specials(power):
            n = pow(10, power)
            while len(l) > 0 and l[-1] in specials:
                l.pop()
            l.append(map[n])

        while cur > 0:
            digit = cur % 10
            cur = cur // 10

            if pos == 3:
                put_specials(index)
                pos = 0

            if digit > -1 and pos == 2:
                l.append(map[100])

            if digit > -1 and pos == 1:
                digit *= 10
                if digit == 10 and prevdigit > 0:
                    l.pop()
                    digit = 10 + prevdigit

            if digit > 0:
                l.append(map[digit])

            pos += 1
            index += 1
            prevdigit = digit

        return ' '.join(l[::-1])

a = Solution()
print(a.numberToWords(0))
print(a.numberToWords(1))
print(a.numberToWords(10))
print(a.numberToWords(20))
print(a.numberToWords(100))
print(a.numberToWords(200))
print(a.numberToWords(1000))
print(a.numberToWords(10000))
print(a.numberToWords(100000))
print(a.numberToWords(100001))
print(a.numberToWords(100100))
print(a.numberToWords(101000))
print(a.numberToWords(110000))
# print(a.numberToWords(1000000))
# print(a.numberToWords(1000000000))
# print(a.numberToWords(17))
# print(a.numberToWords(170))
# print(a.numberToWords(1702))
# print(a.numberToWords(17002))
# print(a.numberToWords(123))
# print(a.numberToWords(12345))
# print(a.numberToWords(1234567))