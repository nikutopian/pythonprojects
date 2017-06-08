# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
def read4(buf):
    buf = ['1','2','3','4']
    return 4

class Solution(object):

    def __init__(self):
        self.index = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 4:
            return read4(buf)




