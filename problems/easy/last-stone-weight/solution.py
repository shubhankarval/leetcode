"""
Problem: Last Stone Weight
Difficulty: Easy
URL: https://leetcode.com/problems/last-stone-weight/

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if y - x:
                heapq.heappush(heap, x - y)

        return -heap[0] if len(heap) else 0
