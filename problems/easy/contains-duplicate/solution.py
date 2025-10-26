"""
Problem: Contains Duplicate
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
