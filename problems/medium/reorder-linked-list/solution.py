"""
Problem: Reorder Linked List
Difficulty: Medium
URL: https://leetcode.com/problems/reorder-list/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        n1, n2 = head, self.reverseList(slow)
        while n1 and n2 and n1.next != n2:
            n1.next, n2.next, n1, n2 = n2, n1.next, n1.next, n2.next

    def reverseList(self, head: Optional[ListNode]):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
