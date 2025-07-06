"""
Problem: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_to_idx:
                return [num_to_idx[diff], i]
            num_to_idx[num] = i

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Brute force approach - check all pairs.

        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        for i in range(len(nums)):
            val = target - nums[i]
            for j in range(i + 1, len(nums)):
                if val == nums[j]:
                    return [i, j]


def test_solution():
    solution = Solution()

    # Test case 1
    result1 = solution.twoSum([2, 7, 11, 15], 9)
    assert result1 == [0, 1], f"Expected [0, 1], got {result1}"

    # Test case 2
    result2 = solution.twoSum([3, 2, 4], 6)
    assert result2 == [1, 2], f"Expected [1, 2], got {result2}"

    # Test case 3
    result3 = solution.twoSum([3, 3], 6)
    assert result3 == [0, 1], f"Expected [0, 1], got {result3}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
