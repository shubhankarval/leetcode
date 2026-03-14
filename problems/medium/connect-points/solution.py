"""
Problem: Min Cost to Connect Points
Difficulty: Medium
URL: https://leetcode.com/problems/min-cost-to-connect-all-points/

Time Complexity: O(n²)
Space Complexity: O(n)
"""

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, cost = len(points), 0
        dist, visited = [float("inf")] * n, [False] * n
        dist[0] = 0

        for _ in range(n):
            # Select: Find the node with the smallest distance to the MST
            u = min((i for i in range(n) if not visited[i]), key=lambda i: dist[i])

            cost += dist[u]
            visited[u] = True
            ux, uy = points[u]

            # Update: Refresh distances from the new node to its neighbors
            for v in range(n):
                if not visited[v]:
                    vx, vy = points[v]
                    new_dist = abs(ux - vx) + abs(uy - vy)
                    if new_dist < dist[v]:
                        dist[v] = new_dist

        return cost

    # Alternative Prim's algorithm (Time Complexity: O(n² log n), Space Complexity: O(n))
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost = 0
        minHeap = [[0, 0]]
        visited = set()

        while len(visited) < n:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            cost += dist
            visited.add(i)
            xi, yi = points[i]

            for j in range(n):
                if j not in visited:
                    xj, yj = points[j]
                    neiDist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, [neiDist, j])

        return cost
