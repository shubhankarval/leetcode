"""
Problem: Kth Largest Element in a Stream
Difficulty: Easy
URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Time Complexity: O(n log k)
Space Complexity: O(k)

where n is the number of calls to the add function and k is the size of the heap.
"""

"""
Intuition:
Maintain minHeap of size k
if new val <= root, dont add new val and return root
else add val to heap, pop root and return new root
"""

import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappush(self.heap, val)
            heapq.heappop(self.heap)
        return self.heap[0]
