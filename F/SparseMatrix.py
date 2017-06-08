class Solution(object):
    def convertToSparse(self, A):
        AS = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    AS.append((i,j, A[i][j]))
        return AS

    def convertToDense(self, AS, A):
        for i,j,v in AS:
            A[i][j] = v


    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        n1,n2 = len(A),len(B)
        if n1 == 0 or n2 == 0:
            return None
        m1,m2 = len(A[0]), len(B[0])

        AS = self.convertToSparse(A)
        BS = self.convertToSparse(B)


        C = [[0] * m2 for _ in range(n1)]

        for i1,j1,v1 in AS:
            for i2,j2,v2 in BS:
                if j1 == i2:
                    C[i1][j2] += v1 * v2

        return C








A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

a = Solution()
print(a.multiply(A, B))


