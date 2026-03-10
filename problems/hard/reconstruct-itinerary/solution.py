"""
Problem: Reconstruct Itinerary
Difficulty: Hard
URL: https://leetcode.com/problems/reconstruct-itinerary/

Time Complexity: O(E log E)
Space Complexity: O(V + E)
- where E = number of tickets
        V = number of unique airports
"""

from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjMap = defaultdict(list)
        for src, dest in tickets:
            adjMap[src].append(dest)

        for src in adjMap:
            adjMap[src].sort(reverse=True)

        path = []

        def dfs(src):
            while adjMap[src]:
                dfs(adjMap[src].pop())
            path.append(src)

        dfs("JFK")
        return path[::-1]
