"""
Problem: Maximum Product Subarray
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-product-subarray/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    # Simple solution - two pass
    def maxProduct(self, nums: List[int]) -> int:
        def get_max_pass(iterator):
            max_prod = float("-inf")
            prod = 1
            has_zero = False

            for num in iterator:
                prod *= num
                max_prod = max(max_prod, prod)

                if num == 0:
                    has_zero = True
                    prod = 1

            return max(max_prod, 0) if has_zero else max_prod

        return max(get_max_pass(nums), get_max_pass(reversed(nums)))

    # Complex solution - one pass
    def maxProduct(self, nums: List[int]) -> int:
        def trim_negative_edge(start, end):
            if end - start == 1:
                return 1
            left = right = 1
            for i in range(start, end):
                left *= nums[i]
                if nums[i] < 0:
                    break
            for i in range(end - 1, start - 1, -1):
                right *= nums[i]
                if nums[i] < 0:
                    break
            return max(left, right)

        start = end = 0
        prod, max_prod = 1, float("-inf")

        for i, num in enumerate(nums):
            if num == 0:
                if start < i:
                    if prod < 0:
                        prod //= trim_negative_edge(start, end)
                    max_prod = max(prod, max_prod)
                max_prod = max(0, max_prod)
                start = end = i + 1
                prod = 1
            else:
                prod *= num
                end += 1

        if start < len(nums):
            if prod < 0:
                prod //= trim_negative_edge(start, end)
            max_prod = max(max_prod, prod)

        return max_prod
