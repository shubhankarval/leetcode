"""
Problem: Kth Largest Element in an Array
Difficulty: Medium
URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

Time Complexity: O(n log k)
Space Complexity: O(k)
where n is the number of elements in nums and k is the kth largest element to find
"""

"""
Intuition:
maintain min heap of size k
if num <= heap[0], ignore
else add to heap and pop
return top element
"""

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [float("-inf")]
        for num in nums:
            if num <= heap[0]:
                continue
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
