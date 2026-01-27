"""
Problem: Graph Valid Tree
Difficulty: Medium
URL: https://neetcode.io/problems/valid-tree/

Time Complexity:  O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V + E) for adjacency list and visited set
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
        visited = set()
        for v1, v2 in edges:
            minV, maxV = min(v1, v2), max(v1, v2)
            if maxV not in visited:
                visited.add(maxV)
                adjList[minV].append(maxV)
            elif minV not in visited:
                visited.add(minV)
                adjList[maxV].append(minV)
            else:
                return False

        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for n in adjList[node]:
                if not dfs(n):
                    return False
            return True

        return dfs(0) and len(visited) == n
