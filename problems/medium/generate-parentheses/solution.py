"""
Problem: Generate Parentheses
Difficulty: Medium
URL: https://leetcode.com/problems/generate-parentheses/

Time Complexity: O(n · Cₙ) where n is the number of pairs of parentheses
Space Complexity: O(n²) for the recursion stack and result storage

- Cₙ = nth Catalan number (~ 4ⁿ / (n^(3/2))).
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()

        def dfs(s):
            if len(s) == n * 2:
                res.add(s)
                return

            for i in range(len(s)):
                if s[i] == "(":
                    dfs(s[: i + 1] + "()" + s[i + 1 :])

            dfs("()" + s)
            dfs(s + "()")

        dfs("()")
        return list(res)
