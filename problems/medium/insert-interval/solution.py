"""
Problem: Insert Interval
Difficulty: Medium
URL: https://leetcode.com/problems/insert-interval/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        start, end = newInterval
        startIdx = endIdx = -1
        i = 0

        while endIdx == -1 and i < len(intervals):
            currStart, currEnd = intervals[i]
            # start
            if startIdx == -1:
                if currStart <= start <= currEnd:
                    startIdx = i
                elif currStart > start:
                    startIdx = i
                    intervals.insert(i, [start, start])
                    continue

            # end
            if currStart <= end <= currEnd:
                endIdx = i
            elif currStart > end:
                endIdx = i
                intervals.insert(i, [end, end])

            i += 1

        if startIdx == -1:
            return intervals + [newInterval]
        if endIdx == -1:
            endIdx = len(intervals)
            intervals.append([end, end])

        return (
            intervals[:startIdx]
            + [[intervals[startIdx][0], intervals[endIdx][1]]]
            + (intervals[endIdx + 1 :] if endIdx != len(intervals) - 1 else [])
        )
