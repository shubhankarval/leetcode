"""
Problem: Palindrome Partitioning
Difficulty: Medium
URL: https://leetcode.com/problems/palindrome-partitioning/

Time Complexity: O(n² * 2ⁿ) where n is the length of the string s
Space Complexity: O(n²) where n is the length of the string s
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, stack = [], []

        def dfs(idx):
            if idx == len(s):
                res.append(stack.copy())
                return

            sub = ""
            for i in range(idx, len(s)):
                sub += s[i]
                if self.isPalindrome(sub):
                    stack.append(sub)
                    dfs(i + 1)
                    stack.pop()

        dfs(0)
        return res

    def isPalindrome(self, s: str) -> bool:
        mid = len(s) // 2
        if len(s) % 2 == 0:
            return s[:mid] == s[mid:][::-1]
        return s[:mid] == s[mid + 1 :][::-1]
