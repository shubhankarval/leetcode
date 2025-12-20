"""
Problem: K Closest Points to Origin
Difficulty: Medium
URL: https://leetcode.com/problems/k-closest-points-to-origin/

Time Complexity: O(n + k log n) where n is number of points and k is number of closest points to return
Space Complexity: O(n) where n is number of points
"""

"""
Intuition:
Get dist for all points from origin to create a list like [[d, [x, y]]...]
heapify this list
return first k elements
"""

import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heap.append([dist, [x, y]])

        heapq.heapify(heap)
        res = []

        while len(res) != k:
            res.append(heapq.heappop(heap)[1])

        return res
