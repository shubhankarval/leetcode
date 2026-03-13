"""
Problem: Min Cost to Connect Points
Difficulty: Medium
URL: https://leetcode.com/problems/min-cost-to-connect-all-points/

Time Complexity: O(n²logn)
Space Complexity: O(n²)
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i, (x1, y1) in enumerate(points):
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])

        cost = 0
        minHeap = [[0, 0]]
        visited = set()

        while len(visited) < len(points):
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            cost += dist
            visited.add(i)

            for neiDist, nei in adjList[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiDist, nei])

        return cost
