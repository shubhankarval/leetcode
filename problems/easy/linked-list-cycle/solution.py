"""
Problem: Linked List Cycle Detection
Difficulty: Easy
URL: https://leetcode.com/problems/linked-list-cycle/
-10⁵ <= Node.val <= 10⁵

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
change each val to a digit
if that digit is visited again return true, else false
"""


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == float("inf"):
                return True
            head.val = float("inf")
            head = head.next
        return False
