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
        res = {"()"}

        for _ in range(2, n + 1):
            s = set()
            for par in res:
                for i in range(len(par)):
                    if par[i] == "(":
                        s.add(par[: i + 1] + "()" + par[i + 1 :])
                s.add("()" + par)
                s.add(par + "()")
            res = s

        return list(res)
