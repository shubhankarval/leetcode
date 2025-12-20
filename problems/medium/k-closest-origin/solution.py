"""
Problem: K Closest Points to Origin
Difficulty: Medium
URL: https://leetcode.com/problems/k-closest-points-to-origin/

Time Complexity: O(n log k)
Space Complexity: O(k)

where n is the number of points and k is the number of closest points to return.
"""

"""
Intuition:
Get dist for all points from origin to create a list like [[d, [x, y]]...]
Use maxheap to store this, and pop if len(maxHeap) > k
"""

import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, [-dist, [x, y]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [pos for _, pos in maxHeap]
