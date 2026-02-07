"""
Problem: House Robber II
Difficulty: Medium
URL: https://leetcode.com/problems/house-robber-ii/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def calc(nums):
            dp = [None] * n

            def rec(i):
                if i >= n:
                    return 0
                if dp[i] == None:
                    dp[i] = max(nums[i] + rec(i + 2), rec(i + 1))
                return dp[i]

            return rec(0)

        return max(calc(nums[: n - 1]), calc(nums[1:]))
