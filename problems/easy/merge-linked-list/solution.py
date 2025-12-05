"""
Problem: Merge Two Sorted Linked Lists
Difficulty: Easy
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Time Complexity: O(n + m) where n and m are the lengths of list1 and list2
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Intuition:
if l1 > l2: add l2 to res, move l2 fwd
else add l1 to res, move l1 fwd
"""


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = res = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                res, list1 = res.next, list1.next
            else:
                res.next = list2
                res, list2 = res.next, list2.next
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        return dummy.next
