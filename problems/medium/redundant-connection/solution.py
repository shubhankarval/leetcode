"""
Problem: Redundant Connection
Difficulty: Medium
URL: https://leetcode.com/problems/redundant-connection/

Time Complexity: O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V + E) for adjacency list, visited array, stack, and cycleNodes set
"""

"""
Intuition:
DFS w/ backtracking
"""

from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        for v1, v2 in edges:
            adjMap[v1].append(v2)
            adjMap[v2].append(v1)

        visited, stack, cycleNodes = [False] * len(edges), [], set()

        def dfs(node, prev):
            if visited[node - 1]:
                idx = -1
                for n in reversed(stack):
                    if n == node:
                        break
                    idx -= 1
                cycleNodes.update(stack[idx:])
                return

            visited[node - 1] = True
            stack.append(node)

            for nei in adjMap[node]:
                if not cycleNodes and nei != prev:
                    dfs(nei, node)

            stack.pop()

        dfs(1, None)
        for v1, v2 in reversed(edges):
            if v1 in cycleNodes and v2 in cycleNodes:
                return [v1, v2]
