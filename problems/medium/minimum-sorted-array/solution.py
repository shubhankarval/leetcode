"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Time Complexity: O(logn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
