class Solution(object):
    def choose_iter(self, elements, length):
        if length == 0:
            yield ()
        for i in range(len(elements)):
            if length == 1:
                yield (elements[i],)
            else:
                for next in self.choose_iter(elements[i+1:len(elements)], length-1):
                    yield (elements[i],) + next

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retval = []
        
        for i in range(0,len(nums)+1):
            for elem in self.choose_iter(nums, i):
                retval.append(list(elem))
        return retval

a  = Solution()
print(a.subsets([1,2,3,4]))
