# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        i = 0

        sintervals = sorted(intervals, key=lambda x: x.start)



        while i < len(sintervals)-1:
            while(i < len(sintervals)-1 and sintervals[i].end >= sintervals[i+1].start):
                sintervals[i+1].start = sintervals[i].start
                if sintervals[i+1].end < sintervals[i].end:
                    sintervals[i+1].end = sintervals[i].end
                sintervals[i] = None
                i += 1
            i += 1

        return [x for x in sintervals if x is not None]




a =Solution()
b = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
for item in a.merge(b):
    print('{0}, {1}'.format(item.start, item.end))

b = [Interval(1,4), Interval(2,3)]
for item in a.merge(b):
    print('{0}, {1}'.format(item.start, item.end))

print()
b = [Interval(41,45), Interval(2,3), Interval(5,7), Interval(43,43), Interval(6,42)]
for item in a.merge(b):
    print('{0}, {1}'.format(item.start, item.end))