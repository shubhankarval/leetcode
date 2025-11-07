"""
Problem: Two Sum II - Input Array is Sorted
Difficulty: Medium
URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            twoSum = numbers[i] + numbers[j]
            if twoSum == target:
                return [i + 1, j + 1]
            elif twoSum < target:
                i += 1
            else:
                j -= 1
