"""
Problem: Minimum Interval to Include Each Query
Difficulty: Hard
URL: https://leetcode.com/problems/minimum-interval-to-include-each-query/

Time Complexity: O(nlogn + n*m)
Space Complexity: O(n)
- where n = length of intervals
        m = length of queries
"""

from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intLength = sorted(
            list(map(lambda x: [x[0], x[1], x[1] - x[0] + 1], intervals)),
            key=lambda x: x[2],
        )
        res = []
        for q in queries:
            res.append(-1)
            for start, end, length in intLength:
                if start <= q <= end:
                    res[-1] = length
                    break
        return res
