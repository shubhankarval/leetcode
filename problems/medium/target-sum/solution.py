"""
Problem: Target Sum
Difficulty: Medium
URL: https://leetcode.com/problems/target-sum/

Time Complexity: O(n * s)
Space Complexity: O(n * s)
- where n = number of elements in nums
        s = sum of all elements in nums
"""

from typing import List


class Solution:
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
