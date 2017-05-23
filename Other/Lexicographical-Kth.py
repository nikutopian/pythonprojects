import random

class Solution(object):
    def pivot(self, arr, start, end):
        randomIndex = random.randint(start, end)
        pivotValue = arr[randomIndex]
        arr[randomIndex],arr[start] = arr[start],arr[randomIndex]
        i,j = start+1,end
        while(i < j):
            while(i < end and arr[i] < pivotValue):
                i+=1
            while(start < j and arr[j] > pivotValue):
                j-=1
            if (i<j):
                arr[i],arr[j] = arr[j],arr[i]

        retindex = start
        if arr[retindex] > arr[j]:
            arr[retindex],arr[j] = arr[j],arr[retindex]
            retindex = j

        return retindex


    def quickSelect(self, arr, start, end, k):
        if start > end:
            return None
        if start == end:
            return arr[start]
        pivotIndex = self.pivot(arr, start, end)
        if pivotIndex == k:
            return arr[k]
        elif pivotIndex > k:
            return self.quickSelect(arr, start, pivotIndex - 1, k)
        else:
            return self.quickSelect(arr, pivotIndex + 1, end, k)

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        arr = [str(x) for x in range(1,n+1)]
        strval = self.quickSelect(arr, 0, len(arr) - 1, k-1)
        return int(strval)


a = Solution()
num = 30
for i in range(0,num):
    print(a.findKthNumber(num,i+1))
