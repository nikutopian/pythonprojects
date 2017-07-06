class Solution:
    def __Combinations_Internal(self, vallist, nstart, n, kstart, k):
        if kstart >= k:
            yield (vallist[:k])
        else:
            for i in range(nstart, n):
                vallist[kstart] = i
                for item in self.__Combinations_Internal(vallist, i+1, n, kstart+1, k):
                    yield item

    def Combinations(self, n, k):
        vallist = [0] * k
        return self.__Combinations_Internal(vallist, 0, n, 0, k)

a = Solution()
print(list(a.Combinations(3,2)))
print()

print(list(a.Combinations(4,2)))
print()

print(list(a.Combinations(5,2)))
print()

print(list(a.Combinations(20,3)))
print()
