"""
Problem: Jump Game
Difficulty: Easy
URL: https://leetcode.com/problems/jump-game/

Time Complexity: O(n²)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None] * len(nums)

        def dfs(i):
            if i + nums[i] >= len(nums) - 1:
                return True
            if dp[i] == None:
                dp[i] = False
                for j in range(1, nums[i] + 1):
                    if dfs(i + j):
                        dp[i] = True
                        break
            return dp[i]

        return dfs(0)
