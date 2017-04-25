__author__ = 'user'
import re

spaceregex = re.compile('[\s]+')

class Stack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        if len(self.arr) == 0:
            return None
        val = self.peek()
        self.arr = self.arr[:-1]
        return val
    def peek(self):
        if len(self.arr) == 0:
            return None
        return self.arr[-1]

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = re.sub(spaceregex, '', s)

        cur_num = 0
        numbers = []
        operations = []
        operation_stack = Stack()

        for c in s:
            if c >= '0' and c <= '9':
                cur_num *= 10
                cur_num += int(c)
            elif c == '-' or c == '+':
                numbers.append(cur_num)
                cur_num = 0
            cur_sign = not (operation_stack.peek() == '-')

            if (c == '-' and cur_sign) or (c == '+' and not cur_sign):
                operations.append('-')
            elif (c == '+' and cur_sign) or (c == '-' and not cur_sign):
                operations.append('+')
            if c == '(' and len(operations) > 0:
                operation_stack.push(operations[-1])
            if c == ')':
                operation_stack.pop()




        numbers.append(cur_num)
        # print(numbers)
        # print(operations)

        assert(len(numbers) == len(operations) + 1)




        sumn = numbers[0]
        for i in range(len(operations)):
            if operations[i] == '-':
                sumn -= numbers[i+1]
            else:
                sumn += numbers[i+1]

        return sumn

        return s

a = Solution()
print(a.calculate('( ( 1 + 1 ) ) - 12+34+9-1'))
print(a.calculate("2-(5-6)"))
print(a.calculate("0"))
print(a.calculate("0-2147483647"))



