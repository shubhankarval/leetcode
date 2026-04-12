"""
Problem: Missing Number
Difficulty: Easy
URL: https://leetcode.com/problems/missing-number/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
