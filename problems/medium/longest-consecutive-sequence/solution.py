"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
URL: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        seq = {}
        for num in nums:
            if num in seq:
                continue
            lst = seq.get(num - 1, []) + [num] + seq.get(num + 1, [])
            for n in lst:
                seq[n] = lst
            print(seq, "\n")

        return max(len(lst) for lst in seq.values())
