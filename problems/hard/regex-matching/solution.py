"""
Problem: Regular Expression Matching
Difficulty: Medium
URL: https://leetcode.com/problems/regular-expression-matching/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m = len(s)
        n = len(p)
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[None] * n for _ in range(m + 1)]

        def dfs(i, j):
            if j == n:
                return i == m

            if dp[i][j] == None:
                ans = False

                if i == m:
                    if p[j] == "*":
                        ans = dfs(i, j + 1)
                    elif j + 1 < n and p[j + 1] == "*":
                        ans = dfs(i, j + 2)

                else:
                    if p[j] == "*":
                        if p[j - 1] == "." or s[i] == p[j - 1]:
                            ans = dfs(i + 1, j)
                        ans = ans or dfs(i, j + 1)
                    elif s[i] == p[j] or p[j] == ".":
                        ans = dfs(i + 1, j + 1)
                        if not ans and j + 1 < n and p[j + 1] == "*":
                            ans = dfs(i, j + 1)
                    elif j + 1 < n and p[j + 1] == "*":
                        ans = dfs(i, j + 2)

                dp[i][j] = ans

            return dp[i][j]

        return dfs(0, 0)
