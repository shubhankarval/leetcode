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
        stack = []
        for t in tokens:
            if t in "+-*/":
                a, b = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[0]
