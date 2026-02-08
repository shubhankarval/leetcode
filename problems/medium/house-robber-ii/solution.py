"""
Problem: House Robber II
Difficulty: Medium
URL: https://leetcode.com/problems/house-robber-ii/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    # DP Bottom-up
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def calc(start, end):
            one = two = three = 0  # 1, 2, 3 houses behind the current house
            for i in range(start, end):
                one, two, three = nums[i] + max(two, three), one, two
            return max(one, two)

        return max(calc(0, len(nums) - 1), calc(1, len(nums)))

    # DP Top-down
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        if not n:
            return nums[0]

        def calc(nums):
            dp = [None] * n

            def rec(i):
                if i >= n:
                    return 0
                if dp[i] == None:
                    dp[i] = max(nums[i] + rec(i + 2), rec(i + 1))
                return dp[i]

            return rec(0)

        return max(calc(nums[:n]), calc(nums[1:]))
