"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
URL: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        while nums_set:
            num = nums_set.pop()
            seq, prev, nxt = 1, num - 1, num + 1
            while prev in nums_set:
                seq += 1
                nums_set.remove(prev)
                prev -= 1
            while nxt in nums_set:
                seq += 1
                nums_set.remove(nxt)
                nxt += 1
            longest_seq = max(longest_seq, seq)

        return longest_seq
