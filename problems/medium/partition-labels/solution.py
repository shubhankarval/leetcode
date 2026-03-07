"""
Problem: Partition Labels
Difficulty: Medium
URL: https://leetcode.com/problems/partition-labels/

Time Complexity: O(n) where n is the length of the string s
Space Complexity: O(u) where u is the number of unique characters in string s
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx = {}  # intervals idx for ch
        intervals = []

        for i, ch in enumerate(s):
            if ch not in idx:
                intervals.append([i, i])
                idx[ch] = len(intervals) - 1
            else:
                intervals[idx[ch]][1] = i

        minStart, maxEnd = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if maxEnd < start:
                res.append(maxEnd - minStart + 1)
                minStart, maxEnd = start, end
            else:
                minStart = min(minStart, start)
                maxEnd = max(maxEnd, end)

        res.append(maxEnd - minStart + 1)
        return res
