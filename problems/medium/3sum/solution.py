"""
Problem: 3Sum
Difficulty: Medium
URL: https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sets = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    lst = [nums[i], nums[j], nums[k]]
                    s = set(lst)
                    if nums[i] + nums[j] + nums[k] == 0 and s not in sets:
                        res.append(lst)
                        sets.append(s)
        return res
