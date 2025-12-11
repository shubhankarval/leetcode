"""
Problem: Merge K Sorted Linked Lists
Difficulty: Hard
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Time Complexity: O(N log k) where N is total number of nodes and k is number of lists
Space Complexity: O(k) for the heap
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


"""
Intuition:
Maintain a sorted data structure 
"""

from typing import List, Optional
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        while heap:
            val, i = heapq.heappop(heap)
            node.next = ListNode(val)
            node, lists[i] = node.next, lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next
