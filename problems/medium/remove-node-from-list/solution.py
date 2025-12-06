"""
Problem: Remove Nth Node From End of Linked List
Difficulty: Medium
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Intuition:
Find length of list
Find element before the one which will be removed 
Handle edge cases: if 1st element
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, node = 0, head
        while node:
            length += 1
            node = node.next

        targetIdx = length - n
        if targetIdx == 0:
            return head.next

        prev, node = head, head.next
        for i in range(targetIdx - 1):
            prev, node = node, node.next

        prev.next = node.next
        return head
