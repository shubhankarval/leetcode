"""
Problem: Cheapest Flights Within K Stops
Difficulty: Medium
URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Time Complexity: O(K * E) where K is the maximum number of stops and E is the number of flights
Space Complexity: O(V + E) where V is the number of cities and E is the number of flights
"""

from collections import deque
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adjList = [[] for _ in range(n)]
        for u, v, p in flights:
            adjList[u].append([v, p])

        inf = float("inf")
        prices = [inf] * n
        prices[src] = 0
        queue = deque([[src, 0, 0]])  # node, cost, hops

        while queue:
            u, cost, hops = queue.popleft()

            if hops <= k:
                for v, p in adjList[u]:
                    newCost = cost + p
                    if newCost < prices[v]:
                        prices[v] = newCost
                        queue.append([v, newCost, hops + 1])

        return prices[dst] if prices[dst] != inf else -1
