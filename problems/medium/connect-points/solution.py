"""
Problem: Min Cost to Connect Points
Difficulty: Medium
URL: https://leetcode.com/problems/min-cost-to-connect-all-points/

Time Complexity: O(n²logn)
Space Complexity: O(n²)
"""

from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = {}  # idx -> sorted list of [dist, idx]
        i = 0
        cost = 0

        for _ in range(len(points) - 1):
            x1, y1 = points[i]
            visited[i] = []

            for j, (x2, y2) in enumerate(points):
                if j not in visited:
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    visited[i].append([dist, j])

            visited[i].sort(reverse=True)
            minDist = float("inf")

            for j in visited:
                while visited[j][-1][1] in visited:
                    visited[j].pop()
                if visited[j][-1][0] < minDist:
                    minDist, i = visited[j][-1]

            cost += minDist

        return cost
