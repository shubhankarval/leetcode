"""
Problem: Clone Graph
Difficulty: Medium
URL: https://leetcode.com/problems/clone-graph/

Time Complexity: O(V + E)
Space Complexity: O(V)
where V is the number of vertices (nodes) and E is the number of edges in the graph.
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
Intuition:
have 1 map for created nodes (k=num, v=node)
have 1 list for nodes yet to be visited
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        clonedNodes = {node.val: Node(node.val)}
        toVisit = [node]

        while toVisit:
            node = toVisit.pop()

            for neighbor in node.neighbors:
                if neighbor.val not in clonedNodes:
                    clonedNodes[neighbor.val] = Node(neighbor.val)
                    toVisit.append(neighbor)
                clonedNodes[node.val].neighbors.append(clonedNodes[neighbor.val])

        return clonedNodes[1]
