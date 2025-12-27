"""
Problem: Letter Combinations of a Phone Number
Difficulty: Medium
URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Time Complexity: O(n * 4^n) where n is the length of the input digits
Space Complexity: O(n) for the recursion stack
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res, stack = [], []
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i == len(digits):
                res.append("".join(stack))
                return
            for ch in letters[digits[i]]:
                stack.append(ch)
                dfs(i + 1)
                stack.pop()

        if digits:
            dfs(0)

        return res
