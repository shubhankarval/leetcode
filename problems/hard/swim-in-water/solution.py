"""
Problem: Swim in Rising Water
Difficulty: Hard
URL: https://leetcode.com/problems/swim-in-rising-water/

Time Complexity: O(n² log n)
Space Complexity: O(n²)
- where n = len(grid)
"""

from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        minHeap = [[grid[0][0], 0, 0]]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while True:
            time, r, c = heapq.heappop(minHeap)
            if r == c == n - 1:
                return time

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(minHeap, [max(time, grid[nr][nc]), nr, nc])
