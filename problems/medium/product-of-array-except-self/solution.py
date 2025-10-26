"""
Problem: Product of Array Except Self
Difficulty: Medium
URL: https://leetcode.com/problems/product-of-array-except-self/

Time Complexity: O(n)
Space Complexity: O(1) - excluding output array
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Optimal approach handling zero cases efficiently.

        Cases:
        - No zeros: divide total product by each element
        - One zero: only the zero position gets the product, others get 0
        - Multiple zeros: all positions get 0

        Time Complexity: O(n)
        Space Complexity: O(1) - excluding output array
        """
        prod, zero_present = 1, False
        for num in nums:
            if num == 0:
                if zero_present:
                    return [0] * len(nums)
                else:
                    zero_present = True
            else:
                prod *= num

        for i, num in enumerate(nums):
            if zero_present:
                if num == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = prod // num

        return nums
