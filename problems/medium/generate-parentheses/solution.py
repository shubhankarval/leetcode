"""
Problem: Generate Parentheses
Difficulty: Medium
URL: https://leetcode.com/problems/generate-parentheses/

Time Complexity: O(n · Cₙ) where n is the number of pairs of parentheses
Space Complexity: O(n) for the recursion stack

- Cₙ = nth Catalan number (~ 4ⁿ / (n^(3/2))).
"""


class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def dfs(s, open_, close):
            if open_ == n and close == n:
                res.append(s)
                return
            if open_ < n:
                dfs(s + "(", open_ + 1, close)
            if close < open_:
                dfs(s + ")", open_, close + 1)

        dfs("", 0, 0)
        return res
