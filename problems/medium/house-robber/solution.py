"""
Problem: House Robber
Difficulty: Medium
URL: https://leetcode.com/problems/house-robber/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    # DP Bottom-Up
    def rob(self, nums: List[int]) -> int:
        one = two = three = 0  # 1, 2, 3 places behind the current index
        for num in nums:
            one, two, three = num + max(two, three), one, two
        return max(one, two)

    # DP Top-Down
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)

        def rec(i):
            if i >= len(nums):
                return 0
            if dp[i] == None:
                dp[i] = max(nums[i] + rec(i + 2), rec(i + 1))
            return dp[i]

        return rec(0)
