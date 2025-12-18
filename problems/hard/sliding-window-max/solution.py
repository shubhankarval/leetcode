"""
Problem: Sliding Window Maximum
Difficulty: Hard
URL: https://leetcode.com/problems/sliding-window-maximum/

Time Complexity: O(n log n) where n is the number of elements in nums
Space Complexity: O(n) for the max heap
"""

import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        maxHeap = [[-nums[i], i] for i in range(k - 1)]
        heapq.heapify(maxHeap)
        res = []

        for i in range(0, len(nums) - k + 1):
            idx = i + k - 1
            heapq.heappush(maxHeap, [-nums[idx], idx])
            res.append(-maxHeap[0][0])
            while not (i + 1 <= maxHeap[0][1] <= idx):
                heapq.heappop(maxHeap)

        return res
