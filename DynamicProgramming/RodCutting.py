import time

class RodCutting:

    def __init__(self, length, price_list):
        if (type(length) != int):
            raise ValueError("length should be int")
        if (type(price_list) != list):
            raise ValueError("price_list should be list")
        self.n = length
        self.p = price_list
        self.aux = [-1000 for _ in range(self.n)]

    def get_optimal_cut_memoized(self, n, p):
        return self.get_optimal_cut_recursive(n, p, True)

    def get_optimal_cut_recursive(self, n, p, memoized=False):
        if n == 0:
            return 0

        if memoized and self.aux[n-1] >= 0:
            return self.aux[n-1]

        q = -10000
        for i in range(min(n,len(p))):
            q = max(q, p[i] + self.get_optimal_cut_recursive(n-i-1, p, memoized))

        if memoized:
            self.aux[n-1] = q
        return q

    def get_optimal_cut(self, methodtype):
        if methodtype == "recursive":
            return self.get_optimal_cut_recursive(self.n, self.p)
        if methodtype == "memoized":
            return self.get_optimal_cut_memoized(self.n, self.p)

price_list = [1,5,8,9,10,17,17,20,24,30]
recursivetime = 0
memoizedtime = 0

for i in range(10,20):
    ob = RodCutting(i, price_list)
    start = time.time()
    ob.get_optimal_cut("recursive")
    end = time.time()
    recursivetime += (end - start)

    start = time.time()
    ob.get_optimal_cut("memoized")
    end = time.time()
    memoizedtime += (end - start)

print(recursivetime)
print(memoizedtime)




