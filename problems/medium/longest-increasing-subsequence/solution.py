"""
Problem: Longest Increasing Subsequence
Difficulty: Medium
URL: https://leetcode.com/problems/longest-increasing-subsequence/

Time Complexity: O(n²) where n is the length of the input array
Space Complexity: O(n) for the dp array and the recursion stack
"""

from typing import List


class Solution:
    # DP Bottom-Up
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1

        return max(dp)

    # DP Top-Down
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        def dfs(i):
            if not dp[i]:
                ans = 1
                for j in range(i + 1, len(nums)):
                    if nums[i] < nums[j]:
                        ans = max(1 + dfs(j), ans)
                dp[i] = ans
            return dp[i]

        maxLen = 0
        for i in range(len(nums)):
            maxLen = max(maxLen, dfs(i))

        return maxLen
