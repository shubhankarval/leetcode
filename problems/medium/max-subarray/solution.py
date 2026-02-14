"""
Problem: Maximum Subarray
Difficulty: Medium
URL: https://leetcode.com/problems/maximum-subarray/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                if currSum < 0:
                    currSum = nums[i]
                else:
                    currSum += nums[i]
            else:
                maxSum = max(currSum, maxSum)
                if currSum + nums[i] >= 0:
                    currSum += nums[i]
                else:
                    currSum = nums[i]

        return max(maxSum, currSum)
