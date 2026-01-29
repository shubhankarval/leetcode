"""
Problem: Graph Valid Tree
Difficulty: Medium
URL: https://neetcode.io/problems/valid-tree/

Time Complexity:  O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V + E) for adjacency list, visited set and recursion stack
"""

"""
Intuition:
dfs through all nodes, if any node repeating then not a tree
if len(visited) != n, then not a tree
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]
        for v1, v2 in edges:
            adjList[v1].append(v2)
            adjList[v2].append(v1)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for child in adjList[node]:
                if child != parent and not dfs(child, node):
                    return False
            return True

        return dfs(0, None) and len(visited) == n
