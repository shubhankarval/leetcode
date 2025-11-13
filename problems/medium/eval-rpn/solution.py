"""
Problem: Evaluate Reverse Polish Notation
Difficulty: Medium
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for t in tokens:
            if t in "+-*/":
                val = int(eval(res[-2] + t + res[-1]))
                res[-2] = str(val)
                res.pop()
            else:
                res.append(t)

        return int(res[-1])
