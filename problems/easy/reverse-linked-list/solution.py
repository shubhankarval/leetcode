"""
Problem: Reverse Linked List
Difficulty: Easy
URL: https://leetcode.com/problems/reverse-linked-list/

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Intuition:
deal with 3 elements at once
prev, curr, next
prev becomes curr
curr points to prev
curr becomes next
"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            p, n = prev, curr.next
            prev = curr
            curr.next = p
            curr = n
        return prev
