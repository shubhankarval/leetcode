"""
Problem: LRU Cache
Difficulty: Medium
URL: https://leetcode.com/problems/lru-cache/

Time Complexity: O(1) for get and put operations
Space Complexity: O(n) where n is the capacity of the LRU cache
"""

from collections import defaultdict


# Doubly Linked List
class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(list)  # key -> [value, node]
        self.head = Node("head")
        self.tail = Node("tail", self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        # update list
        if key in self.cache:
            self.updateNode(key)
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        # add to list or update list, delete from list if breaching capacity
        if key in self.cache:
            self.cache[key][0] = value
            self.updateNode(key)
        else:
            self.cache[key].append(value)
            if len(self.cache) > self.capacity:
                self.deleteHead()
            self.addTail(key)
            self.cache[key].append(self.tail.prev)

    def addTail(self, key: int):
        node = Node(key, self.tail.prev, self.tail)
        self.tail.prev.next = self.tail.prev = node

    def updateNode(self, key: int):
        # delete node
        node = self.cache[key][1]
        node.prev.next = node.next
        node.next.prev = node.prev

        # add to tail
        self.addTail(key)
        self.cache[key][1] = self.tail.prev

    def deleteHead(self):
        del self.cache[self.head.next.key]
        node = self.head.next.next
        self.head.next = node
        node.prev = self.head
