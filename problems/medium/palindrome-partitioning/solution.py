"""
Problem: Palindrome Partitioning
Difficulty: Medium
URL: https://leetcode.com/problems/palindrome-partitioning/

Time Complexity: O(n * 2ⁿ) where n is the length of the string s
Space Complexity: O(n) where n is the length of the string s
"""

from typing import List

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

    def isPalindrome(self, sub: str) -> bool:
        l, r = 0, len(sub) - 1
        while l < r:
            if sub[l] != sub[r]:
                return False
            l, r = l + 1, r - 1
        return True