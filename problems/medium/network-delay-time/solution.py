"""
Problem: Network Delay Time
Difficulty: Medium
URL: https://leetcode.com/problems/network-delay-time/

Time Complexity: O(E log V) where E is the number of edges and V is the number of vertices
Space Complexity: O(E + V) for the adjacency list, min heap and visited set
"""

from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adjList[u].append([v, t])

        minHeap = [[0, k]]  # time, node
        visited = set()
        time = 0

        while minHeap and len(visited) < n:
            t, u = heapq.heappop(minHeap)
            if u in visited:
                continue
            visited.add(u)
            time = t

            for v, t in adjList[u]:
                if v not in visited:
                    heapq.heappush(minHeap, [time + t, v])

        return time if len(visited) == n else -1
