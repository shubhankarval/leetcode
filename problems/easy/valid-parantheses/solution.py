"""
Problem: Valid Parentheses
Difficulty: Easy
URL: https://leetcode.com/problems/valid-parentheses/

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                stack.append(bracket)
            elif len(stack):
                last_open_bracket = stack.pop()
                if ord(last_open_bracket) // 10 != ord(bracket) // 10:
                    return False
            else:
                return False

        return len(stack) == 0
