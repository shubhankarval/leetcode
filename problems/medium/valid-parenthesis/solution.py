"""
Problem: Valid Parenthesis String
Difficulty: Medium
URL: https://leetcode.com/problems/valid-parenthesis-string/

Time Complexity: O(n²)
Space Complexity: O(n²)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(i, c):
            if c < 0:
                return False
            if i == len(s):
                return c == 0
            if (i, c) in dp:
                return dp[(i, c)]

            if s[i] == "(":
                dp[(i, c)] = dfs(i + 1, c + 1)
            elif s[i] == ")":
                dp[(i, c)] = dfs(i + 1, c - 1)
            else:
                dp[(i, c)] = dfs(i + 1, c + 1) or dfs(i + 1, c - 1) or dfs(i + 1, c)

            return dp[(i, c)]

        return dfs(0, 0)
