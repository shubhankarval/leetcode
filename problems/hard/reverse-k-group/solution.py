"""
Problem: Reverse Nodes in K-Group
Difficulty: Hard
URL: https://leetcode.com/problems/reverse-nodes-in-k-group/

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
Use two pointers
First will go till k elements
if k elements exists, second point will do reversal till kth element
"""


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev, curr = None, head
        res, reversals = head, 0
        while curr:
            start = end = curr
            l = 0
            while end:
                l += 1
                if l == k:
                    break
                end = end.next
            if l != k:
                break

            prevStart, newStart = prev, end.next
            while curr != newStart:
                curr.next, prev, curr = prev, curr, curr.next

            reversals += 1
            if reversals == 1:
                res = end
            else:
                prevStart.next = prev

            prev = start
            prev.next = newStart

        return res
