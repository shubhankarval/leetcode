"""
Problem: Non-overlapping Intervals
Difficulty: Medium
URL: https://leetcode.com/problems/non-overlapping-intervals/

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0  # no. of overlapping intervals
        i, n = 0, len(intervals)

        while i < n:
            prevInterval = intervals[i]
            j = i + 1
            while j < n and prevInterval[1] > intervals[j][0]:
                if prevInterval[1] > intervals[j][1]:
                    prevInterval = intervals[j]
                j += 1
            res += j - i - 1
            i = j

        return res
