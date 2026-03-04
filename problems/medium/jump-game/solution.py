"""
Problem: Jump Game
Difficulty: Medium
URL: https://leetcode.com/problems/jump-game/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= t:
                t = i
        return t == 0

    # Alternative solution (O(n²) time, O(1) space)
    def canJump(self, nums: List[int]) -> bool:
        i, n = 0, len(nums)
        while i < n:
            maxJ = nxt = 0

            for j in range(i, i + nums[i] + 1):
                currJ = nums[j] + j
                if currJ >= n - 1:
                    return True
                if nums[j] == 0:
                    continue
                if currJ >= maxJ:
                    maxJ = currJ
                    nxt = j

            if i == nxt:
                return False
            i = nxt

        return False
