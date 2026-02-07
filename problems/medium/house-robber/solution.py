"""
Problem: House Robber
Difficulty: Medium
URL: https://leetcode.com/problems/house-robber/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)

        def rec(i):
            if i >= len(nums):
                return 0
            if dp[i] == None:
                dp[i] = max(nums[i] + rec(i + 2), rec(i + 1))
            return dp[i]

        return rec(0)
