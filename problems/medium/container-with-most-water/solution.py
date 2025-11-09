"""
Problem: Container With Most Water
Difficulty: Medium
URL: https://leetcode.com/problems/container-with-most-water/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            h1, h2 = heights[l], heights[r]
            area = max(area, min(h1, h2) * (r - l))
            if h1 < h2:
                l += 1
            elif h1 > h2:
                r -= 1
            else:
                l += 1
                r -= 1
        return area
