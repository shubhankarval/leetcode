"""
Problem: Partition Equal Subset Sum
Difficulty: Medium
URL: https://leetcode.com/problems/partition-equal-subset-sum/

Time Complexity: O(n * s) where n is the length of nums and s is the half-sum of nums
Space Complexity: O(s) for the set of sums
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if len(nums) == 1 or total % 2 != 0:
            return False

        target = total // 2
        sums = set([0])
        for i in range(len(nums) - 1, -1, -1):
            if target - nums[i] in sums:
                return True
            newSums = []
            for s in sums:
                if s + nums[i] < target:
                    newSums.append(s + nums[i])
            sums.update(newSums)

        return False
