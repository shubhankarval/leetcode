"""
Problem: Daily Temperatures
Difficulty: Medium
URL: https://leetcode.com/problems/daily-temperatures/

Time Complexity: O(n²)
Space Complexity: O(1)
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i, j = 0, 1
        res = []
        while i < len(temperatures):
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                j += 1
            if j == len(temperatures):
                res.append(0)
            else:
                res.append(j - i)
            i += 1
            j = i + 1

        return res
