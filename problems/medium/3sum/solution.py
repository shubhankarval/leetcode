"""
Problem: 3Sum
Difficulty: Medium
URL: https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, seen = [], set()
        num_idx = self.create_index_map(nums)

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                target = 0 - (nums[i] + nums[j])
                fs = frozenset([nums[i], nums[j], target])
                if fs in seen:
                    continue
                seen.add(fs)
                if target in num_idx and self.check_dup_idx(num_idx[target], i, j):
                    res.append([nums[i], nums[j], target])
        return res

    def create_index_map(self, lst: List[int]):
        index_map = {}
        for i, val in enumerate(lst):
            if val not in index_map:
                index_map[val] = set()
            index_map[val].add(i)
        return index_map

    def check_dup_idx(self, s: set, num1: int, num2: int) -> bool:
        if (num1 in s and num2 not in s) or (num1 not in s and num2 in s):
            return len(s) > 1
        elif num1 in s and num2 in s:
            return len(s) > 2
        return True
