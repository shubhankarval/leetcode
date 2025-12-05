"""
Problem: Linked List Cycle Detection
Difficulty: Easy
URL: https://leetcode.com/problems/linked-list-cycle/
-1000 <= Node.val <= 1000

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
            if head.val == 1001:
                return True
            head.val = 1001
            head = head.next
        return False
