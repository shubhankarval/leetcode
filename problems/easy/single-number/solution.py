"""
Problem: Single Number
Difficulty: Easy
URL: https://leetcode.com/problems/single-number/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
