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


def test_solution():
    solution = Solution()

    # Test case 1: Basic case
    result1 = solution.productExceptSelf([1, 2, 3, 4])
    expected1 = [24, 12, 8, 6]
    assert result1 == expected1, f"Expected {expected1}, got {result1}"

    # Test case 2: With negative numbers
    result2 = solution.productExceptSelf([-1, 1, 0, -3, 3])
    expected2 = [0, 0, 9, 0, 0]
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    # Test case 3: Single zero
    result3 = solution.productExceptSelf([1, 0, 3, 4])
    expected3 = [0, 12, 0, 0]
    assert result3 == expected3, f"Expected {expected3}, got {result3}"

    # Test case 4: Multiple zeros
    result4 = solution.productExceptSelf([0, 0, 2, 3])
    expected4 = [0, 0, 0, 0]
    assert result4 == expected4, f"Expected {expected4}, got {result4}"

    # Test case 5: All ones
    result5 = solution.productExceptSelf([1, 1, 1, 1])
    expected5 = [1, 1, 1, 1]
    assert result5 == expected5, f"Expected {expected5}, got {result5}"

    # Test case 6: Two elements
    result6 = solution.productExceptSelf([2, 3])
    expected6 = [3, 2]
    assert result6 == expected6, f"Expected {expected6}, got {result6}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
