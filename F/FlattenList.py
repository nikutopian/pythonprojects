# class NestedInteger(object):
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.currentList = nestedList

        self.nestedStack = []

        for item in nestedList:
            self.nestedStack.append(item)




    def nextElem(self, l):
        for item in l:
            if type(item) is int:
                yield item
            elif type(item) is list:
                for item2 in self.nextElem(item):
                    yield item2

    def next(self):
        """
        :rtype: int
        """

        if self.hasNext():
            return self.nestedStack.pop().getInteger()

        # return self.nextElem(self.nestedList)

        

    def hasNext(self):
        """
        :rtype: bool
        """
        while (len(self.nestedStack) > 0):
            top = self.nestedStack[0]
            if (top.isInteger()):
                return True
            else:
                top = self.nestedStack.pop().getList()
                for i in range(len(top) - 1, -1, -1):
                    self.nestedStack.insert(0, top[i])

        return False


a = NestedIterator([1,2,[3,4,[18,21],5],[7]])
for item in a.next():
    print(item)

