"""
Problem: Merge Interval
Difficulty: Medium
URL: https://leetcode.com/problems/merge-intervals/

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        i, n = 0, len(intervals)
        res = []

        while i < n:
            j = i + 1
            while j < n and intervals[j][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                j += 1
            res.append(intervals[i])
            i = j

        return res
