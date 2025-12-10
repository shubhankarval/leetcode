"""
Problem: Copy Linked List with Random Pointer
Difficulty: Medium
URL: https://leetcode.com/problems/copy-list-with-random-pointer/

Time Complexity: O(n)
Space Complexity: O(n)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        n1 = head
        dummy = n2 = Node(0)
        nodes = {}  # n1 to n2
        while n1:
            if n1 in nodes:
                n2.next = nodes[n1]
            else:
                nodes[n1] = n2.next = Node(n1.val)
            n2 = n2.next
            if n1.random in nodes:
                n2.random = nodes[n1.random]
            elif n1.random:
                nodes[n1.random] = n2.random = Node(n1.random.val)
            n1 = n1.next
        return dummy.next
