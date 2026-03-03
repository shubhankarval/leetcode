"""
Problem: Jump Game II
Difficulty: Easy
URL: https://leetcode.com/problems/jump-game-ii/

Time Complexity: O(n²)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        i = jumps = 0

        while i < n:
            if i + nums[i] >= n - 1:
                return jumps + 1

            maxJ = nxt = 0
            for j in range(i + 1, i + nums[i] + 1):
                if nums[j] == 0:
                    continue
                currJ = nums[j] + j
                if currJ >= maxJ:
                    maxJ, nxt = currJ, j
            i = nxt
            jumps += 1
