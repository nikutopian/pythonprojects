__author__ = 'user'

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        names = input.split('\n')
        curlevel = 0

        lengths = []
        max = 0

        for name in names:
            level = 0

            while name.startswith('\t'):
                level += 1
                name = name[1:]

            while len(lengths) > level:
                lengths.pop()

            total_length = 0
            if len(lengths) > 0:
                total_length = lengths[-1] + 1

            lengths.append(total_length + len(name))

            if '.' in name and max < total_length + len(name):
                max = total_length + len(name)


        return max


a = Solution()
print(a.lengthLongestPath("a"))
print(a.lengthLongestPath("dir\n\tfiledir\n\t\tfile"))
print(a.lengthLongestPath("dir\n\tfiledir\n\t\tf.il"))
print(a.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(a.lengthLongestPath("aaaaaaaaaaaaaaaaaaaaaa\n\tsthpngpngpng\naaaaaaaaaaaaaaaaaaaaaa\n\tsth.png\na\n\taa\n\t\taaa\n\t\t\tfile1.txt"))




