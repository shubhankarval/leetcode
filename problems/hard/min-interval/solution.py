"""
Problem: Minimum Interval to Include Each Query
Difficulty: Hard
URL: https://leetcode.com/problems/minimum-interval-to-include-each-query/

Time Complexity: O(nlogn + n*k + m)
Space Complexity: O(k)
- where n = length of intervals
        m = length of queries
        k = max - min time in intervals
"""

from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[1] - x[0])
        out = {}  # time -> len

        for start, end in intervals:
            diff = end - start + 1
            for i in range(start, end + 1):
                if i not in out:
                    out[i] = diff

        return [out[time] if time in out else -1 for time in queries]
