class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.cursize = 0
        self.avg = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.cursize < self.size:
            self.avg = ((self.avg * self.cursize) + val) / (self.cursize + 1)
            self.cursize += 1
        else:
            self.avg += ((val - self.avg) / self.cursize)
        return self.avg
            

a = MovingAverage(4)
for i in range(1,10):
    print(a.next(i))

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)