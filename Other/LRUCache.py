__author__ = 'user'

class QueueNode:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.value = val

class LRUCache(object):


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.count = 0
        self.mapper = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.mapper:
            return -1

        node = self.mapper[key]
        val = node.value

        self.deletenode(node)
        self.addnode(QueueNode(key, val))

        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key in self.mapper:
            self.deletenode(self.mapper[key])

        self.addnode(QueueNode(key, value))

    def addnode(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            headnode = self.head
            node.next = headnode
            headnode.prev = node
            self.head = node
        self.mapper[node.key] = node
        self.count += 1
        if self.count > self.capacity:
            self.dequeue()

    def dequeue(self):
        if self.tail is not None:
            self.deletenode(self.tail)
        if self.count == 0:
            self.head = self.tail = None

    def deletenode(self, node):
        if node is None:
            return
        key = node.key
        del self.mapper[key]
        prevnode = node.prev
        nextnode = node.next
        if prevnode is not None:
            prevnode.next = nextnode
        if nextnode is not None:
            nextnode.prev = prevnode
        if self.tail == node:
            self.tail = prevnode
        if self.head == node:
            self.head = nextnode

        self.count -= 1

    # def enqueue(self, key, value):
    #
    #     node = QueueNode(key, value)
    #     if self.head is None:
    #         self.head = self.tail = node
    #     else:
    #         headnode = self.head
    #         node.next = headnode
    #         headnode.prev = node
    #         self.head = node
    #
    #     self.count += 1
    #     if self.count > self.capacity:
    #         self.count -= 1
    #         self.dequeue()
    #
    #     return node
    #
    #
    # def dequeue(self):
    #     val = None
    #     if self.tail is not None:
    #         val = self.tail.value
    #         key = self.tail.key
    #         del self.mapper[key]
    #         prevnode = self.tail.prev
    #         if prevnode is not None:
    #             prevnode.next = None
    #         self.tail = prevnode
    #
    #     return val

# cache = LRUCache(2);
#
# print(cache.put(1, 1))
# print(cache.put(2, 2))
# print(cache.get(1))       # returns 1
# print(cache.put(3, 3))    # evicts key 2
# print(cache.get(2))       # returns -1 (not found)
# print(cache.put(4, 4))    # evicts key 1
# print(cache.get(1))       # returns -1 (not found)
# print(cache.get(3))       # returns 3
# print(cache.get(4))       # returns 4

# cache = LRUCache(10)
# print(cache.put(7,28))
# print(cache.put(7,1))
# print(cache.put(8,15))
# print(cache.get(6))
# print(cache.put(10,27))
# print(cache.put(8,10))
# print(cache.get(8))
# print(cache.put(6,29))
# print(cache.put(1,9))
# print(cache.get(6))
# print(cache.put(10,7))
# print(cache.get(1))
# print(cache.get(2))
# print(cache.get(13))
# print(cache.put(8,30))
# print(cache.put(1,5))
# print(cache.get(1))
# print(cache.put(13,2))
# print(cache.get(12))


cache = LRUCache(2)
print(cache.put(2,2))
print(cache.put(1,1))
print(cache.put(3,3))
print(cache.get(1))
print(cache.put(4,4))
print(cache.get(3))
print(cache.get(2))
print(cache.get(4))