"""
Problem: Contains Duplicate
Difficulty: Easy
URL: https://leetcode.com/problems/contains-duplicate/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


def test_solution():
    solution = Solution()

    # Test case 1: Contains duplicates
    result1 = solution.containsDuplicate([1, 2, 3, 1])
    assert result1 == True, f"Expected True, got {result1}"

    # Test case 2: No duplicates
    result2 = solution.containsDuplicate([1, 2, 3, 4])
    assert result2 == False, f"Expected False, got {result2}"

    # Test case 3: All same elements
    result3 = solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    assert result3 == True, f"Expected True, got {result3}"

    # Test case 4: Single element
    result4 = solution.containsDuplicate([1])
    assert result4 == False, f"Expected False, got {result4}"

    # Test case 5: Empty array
    result5 = solution.containsDuplicate([])
    assert result5 == False, f"Expected False, got {result5}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
