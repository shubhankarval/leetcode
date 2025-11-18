"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/

Time Complexity: O(logn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[l] < nums[r]:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < target:
                    if nums[m] > nums[-1]:
                        l = m + 1
                    else:
                        if target > nums[-1]:
                            r = m - 1
                        else:
                            l = m + 1
                else:
                    if nums[m] < nums[-1]:
                        r = m - 1
                    else:
                        if target > nums[-1]:
                            r = m - 1
                        else:
                            l = m + 1

        return l if nums[l] == target else -1
