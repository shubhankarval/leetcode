"""
Problem: Maximum Product Subarray
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-product-subarray/

Time Complexity: O(n²)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums)):
            prod = maxProd = nums[i]
            for j in range(i + 1, len(nums)):
                prod *= nums[j]
                maxProd = max(prod, maxProd)
            res = max(res, maxProd)
        return res
