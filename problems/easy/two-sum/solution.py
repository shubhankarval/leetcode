"""
Problem: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_idx:
                return [num_to_idx[diff], i]
            num_to_idx[num] = i

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach - check all pairs.

        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            val = target - nums[i]
            for j in range(i + 1, len(nums)):
                if val == nums[j]:
                    return [i, j]