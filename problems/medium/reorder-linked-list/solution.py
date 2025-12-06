"""
Problem: Reorder Linked List
Difficulty: Medium
URL: https://leetcode.com/problems/reorder-list/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next

        l, r = 0, len(lst) - 1
        while l < r:
            lst[l].next, lst[r].next = lst[r], lst[l].next
            l += 1
            r -= 1
        lst[l].next = None
