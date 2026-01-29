"""
Problem: Count Connected Components in an Undirected Graph
Difficulty: Medium
URL: https://neetcode.io/problems/count-connected-components/

Time Complexity: O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V + E) for the adjacency list, visited array, and recursion stack
"""

"""
Intuition:
Use DFS to visit all nodes in a component
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            for nei in adjList[node]:
                if not visited[nei]:
                    dfs(nei)

        count = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1

        return count
