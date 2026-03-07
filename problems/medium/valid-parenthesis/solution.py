"""
Problem: Valid Parenthesis String
Difficulty: Medium
URL: https://leetcode.com/problems/valid-parenthesis-string/

Time Complexity: O(n³)
Space Complexity: O(n²)
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = {}

        def dfs(i, c):
            if i == len(s):
                return c == 0
            if (i, c) in dp:
                return dp[(i, c)]
            x = c
            star = False
            for j in range(i, len(s)):
                if x < 0:
                    break
                if s[j] == "(":
                    x += 1
                elif s[j] == ")":
                    x -= 1
                else:
                    dp[(i, c)] = dfs(j + 1, x + 1) or dfs(j + 1, x - 1) or dfs(j + 1, x)
                    star = True
                    break
            if not star:
                dp[(i, c)] = x == 0
            return dp[(i, c)]

        return dfs(0, 0)
