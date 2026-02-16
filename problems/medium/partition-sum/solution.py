"""
Problem: Partition Equal Subset Sum
Difficulty: Medium
URL: https://leetcode.com/problems/partition-equal-subset-sum/

Time Complexity: O(n² * t) where n is the length of nums and t is the half-sum of nums array
Space Complexity: O(n * t) for dp dict and recursion stack
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if len(nums) == 1 or total % 2 != 0:
            return False

        target = total // 2
        dp = {}

        def dfs(i, total):
            if (i, total) not in dp:
                dp[(i, total)] = False
                if total == target:
                    dp[(i, total)] = True
                elif total < target:
                    for j in range(i + 1, len(nums)):
                        if dfs(j, total + nums[j]):
                            dp[(i, total)] = True
                            break
            return dp[(i, total)]

        return dfs(-1, 0)
