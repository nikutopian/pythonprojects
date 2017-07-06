class Solution:
    # Heap's algorithm
    def __Permutations_Internal(self, n, a):
        if n == 1:
            yield a[:]
        else:
            for i in range(n):
                for item in self.__Permutations_Internal(n-1, a):
                    yield item
                if n % 2 == 0:
                    a[i],a[n-1] = a[n-1],a[i]
                else:
                    a[0],a[n-1] = a[n-1],a[0]

    def __Permutations_Internal2(self, a, low=0):
        if low >= len(a) - 1:
            yield a[:]
        else:
            for p in self.__Permutations_Internal2(a, low + 1):
                yield p
            for i in range(low + 1, len(a)):
                a[low], a[i] = a[i], a[low]
                for p in self.__Permutations_Internal2(a, low + 1):
                    yield p
                a[low], a[i] = a[i], a[low]

    def Permutations(self, n):
        a = list(range(n))
        return self.__Permutations_Internal(n, a)
        #return self.__Permutations_Internal2(a)




import time

a = Solution()
s = time.time()
print(len(list(a.Permutations(7))))
print(time.time() - s)

print()

