"""
Problem: Redundant Connection
Difficulty: Medium
URL: https://leetcode.com/problems/redundant-connection/

Time Complexity: O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V + E) for adjacency list, visited array, stack, and cycle set
"""

"""
Intuition:
DFS w/ backtracking
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = [[] for _ in range(n + 1)]
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = [False] * (n + 1)
        cycle = set()
        stack = []

        def dfs(node, prev):
            if visited[node]:
                idx = len(stack) - 1
                while stack[idx] != node:
                    idx -= 1
                cycle.update(stack[idx:])
                return

            visited[node] = True
            stack.append(node)

            for nei in adjList[node]:
                if not cycle and nei != prev:
                    dfs(nei, node)

            stack.pop()

        dfs(1, None)
        for v1, v2 in reversed(edges):
            if v1 in cycle and v2 in cycle:
                return [v1, v2]
