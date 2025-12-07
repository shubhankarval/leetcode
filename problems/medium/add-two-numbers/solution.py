"""
Problem: Add Two Numbers
Difficulty: Medium
URL: https://leetcode.com/problems/add-two-numbers/

Time Complexity: O(max(m, n)) where m and n are the lengths of the two lists
Space Complexity: O(1)
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = node = ListNode()
        rem = 0

        while l1 or l2 or rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            s = rem + val1 + val2
            node.next = ListNode(s % 10)
            rem = s // 10

            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
