# Definition for an interval.

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        sintervals = sorted(intervals, key=lambda x: x.start)

        minvals = []


        for interval in sintervals:
            index = 0
            while len(minvals) > index and minvals[index] > interval.start:
                index += 1
            if len(minvals) <= index:
                minvals.append(interval.end)
            else:
                minvals[index] = interval.end

        return len(minvals)

a = Solution()
print(a.minMeetingRooms([Interval(0,30), Interval(5,10), Interval(15,20), Interval(16,25)]))