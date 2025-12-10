"""
Problem: Merge K Sorted Linked Lists
Difficulty: Hard
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Time Complexity: O(n * k) where n is the total number of nodes and k is the number of lists
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Intuition:
For each iteration: 
go through each node in list, keep track of node with smallest val
add node to new list, move node to next
"""

from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = res = ListNode()
        while True:
            minNode, minIdx = ListNode(float("inf")), -1
            for idx, node in enumerate(lists):
                if node and node.val < minNode.val:
                    minNode = node
                    minIdx = idx
            if minIdx == -1:
                break
            res.next = minNode
            res, lists[minIdx] = res.next, lists[minIdx].next
        return dummy.next
