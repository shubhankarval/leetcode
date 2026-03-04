"""
Problem: Jump Game II
Difficulty: Medium
URL: https://leetcode.com/problems/jump-game-ii/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        start = 0  # idx to start scan
        end = nums[0]
        max1 = 0  # curr max
        jumps = 1

        while start < n:
            if start + nums[start] >= n - 1:
                return jumps

            max2 = 0  # max to be found

            for i in range(start, end + 1):
                if nums[i] == 0:
                    continue

                curr = nums[i] + i
                if curr >= n - 1:
                    return jumps + 1

                if curr >= max1:
                    max1 = curr
                    max2 = 0
                elif curr >= max2:
                    max2 = curr

            start = end
            end = max1
            max1 = max2
            jumps += 1
