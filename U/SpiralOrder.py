class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        istart = jstart = 0
        iend = m - 1
        jend = n - 1

        output = []
        while istart <= iend and jstart <= jend:
            i = istart
            j = jstart

            while (j <= jend):
                output.append(matrix[i][j])
                j += 1
            istart += 1

            if (istart > iend):
                break

            i = istart
            j = jend

            while (i <= iend):
                output.append(matrix[i][j])
                i += 1
            jend -= 1

            if (jstart > jend):
                break

            i = iend
            j = jend

            while (j >= jstart):
                output.append(matrix[i][j])
                j -= 1
            iend -= 1

            if (istart > iend):
                break

            i = iend
            j = jstart

            while (i >= istart):
                output.append(matrix[i][j])
                i -= 1
            jstart += 1

            if (jstart > jend):
                break



        return output

a = Solution()
print(a.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
print(a.spiralOrder([[ 2, 3 ]]))



