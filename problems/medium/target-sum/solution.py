"""
Problem: Target Sum
Difficulty: Medium
URL: https://leetcode.com/problems/target-sum/

Time Complexity: O(n * s)
Space Complexity: O(s)
- where n = number of elements in nums
        s = sum of all elements in nums
"""

from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # amount -> count

        for num in nums:
            dp2 = defaultdict(int)
            for amt in dp:
                dp2[amt + num] += dp[amt]
                dp2[amt - num] += dp[amt]
            dp = dp2

        return dp[target] if target in dp else 0

    # DP Top-Down (Space Complexity: O(n * s))
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, amt):
            if i == n:
                return 1 if amt == target else 0
            if (i, amt) not in dp:
                dp[(i, amt)] = dfs(i + 1, amt + nums[i]) + dfs(i + 1, amt - nums[i])
            return dp[(i, amt)]

        return dfs(0, 0)
