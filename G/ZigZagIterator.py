class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.index = 0
        self.lists = [v1, v2]
        lenlists = [len(x) for x in self.lists]
        self.total_len = sum(lenlists)
        self.min_len = min(lenlists)
        self.max_index = max(list(range(len(lenlists))), key=lambda x: lenlists[x])

    def __getlistindex(self, index):
        if index >= self.total_len:
            return None, None
        if index >= self.min_len * 2:
            return self.max_index, (index - self.min_len)
        else:
            return index % 2, (index // 2)



    def next(self):
        """
        :rtype: int
        """
        listindex, index = self.__getlistindex(self.index)
        if listindex is not None:
            self.index += 1
            return self.lists[listindex][index]

        return None





    def hasNext(self):
        """
        :rtype: bool
        """
        nextindex,_ = self.__getlistindex(self.index)
        return nextindex is not None

# # Your ZigzagIterator object will be instantiated and called as such:
# # i, v = ZigzagIterator(v1, v2), []
# # while i.hasNext(): v.append(i.next())
#
# a = ZigzagIterator([1,2,3,4,5,6], [10,20])
# while a.hasNext():
#     print(a.next())


class ZigzagIterator(object):

    def __init__(self, vlists):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.index = 0
        self.lists = vlists
        len_list = [len(x) for x in self.lists]
        self.total_len = sum(len_list)
        len_list = sorted(set(len_list))
        self.index_lists = [[i for i in range(len(self.lists)) if len(self.lists[i]) >= l] for l in len_list]
        self.cum_len_list = []
        len_so_far = 0
        sum_so_far = 0
        for i in range(0, len(len_list)):
            diff_len = len_list[i] - len_so_far
            len_so_far = len_list[i]
            sum_so_far += diff_len * len(self.index_lists[i])
            self.cum_len_list.append(sum_so_far)
        self.len_list = len_list
        self.cum_index = 0

        # print(self.index_lists)
        # print(self.cum_len_list)
        # print(self.len_list)


    def __getlistindex(self, index):
        if index >= self.total_len:
            return None, None
        if index >= self.cum_len_list[self.cum_index]:
            self.cum_index += 1
        diff_index = index
        curr_len = 0
        if self.cum_index > 0:
            diff_index -= self.cum_len_list[self.cum_index - 1]
            curr_len = self.len_list[self.cum_index - 1]

        active_indices = self.index_lists[self.cum_index]
        j = curr_len +  diff_index // len(active_indices)
        k = diff_index % len(active_indices)
        i = active_indices[k]
        return i,j



    def next(self):
        """
        :rtype: int
        """
        listindex, index = self.__getlistindex(self.index)
        if listindex is not None:
            self.index += 1
            return self.lists[listindex][index]

        return None





    def hasNext(self):
        """
        :rtype: bool
        """
        nextindex,_ = self.__getlistindex(self.index)
        return nextindex is not None

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

a = ZigzagIterator([[1,2,3,4,5,6], [10,20], [100, 200,300,400,500,600,700,800,900], [9876]])
# a = ZigzagIterator([[1,2,3,4,5,6], [10,20]])
while a.hasNext():
    print(a.next())
