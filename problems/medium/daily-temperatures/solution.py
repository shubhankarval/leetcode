"""
Problem: Daily Temperatures
Difficulty: Medium
URL: https://leetcode.com/problems/daily-temperatures/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
