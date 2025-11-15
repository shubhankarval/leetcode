"""
Problem: Binary Search
Difficulty: Easy
URL: https://leetcode.com/problems/binary-search/

Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
