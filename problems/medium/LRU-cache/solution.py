"""
Problem: LRU Cache
Difficulty: Medium
URL: https://leetcode.com/problems/lru-cache/

Time Complexity: O(1) for get and put operations
Space Complexity: O(n) where n is the capacity of the LRU cache
"""


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyVal = {}
        self.keyNode = {}
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key in self.keyVal:
            self.updateNode(key)
            return self.keyVal[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyVal:
            self.updateNode(key)
        else:
            if len(self.keyVal) + 1 > self.capacity:
                del self.keyVal[self.head.val]
                self.deleteNode()
            self.addNode(key)
        self.keyVal[key] = value

    def addNode(self, key: int):
        # Add new tail node
        if not self.head:
            self.head = self.tail = Node(key)
        else:
            self.tail.next = Node(key, self.tail)
            self.tail = self.tail.next
        self.keyNode[key] = self.tail

    def updateNode(self, key: int):
        # delete curr node & add new tail node
        node = self.keyNode[key]
        if node == self.head:
            self.deleteNode()
        elif node == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.addNode(key)

    def deleteNode(self):
        # Delete head node
        key = self.head.val
        del self.keyNode[key]
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = self.tail = None
