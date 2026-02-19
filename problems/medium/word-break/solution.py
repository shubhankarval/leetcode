"""
Problem: Word Break
Difficulty: Medium
URL: https://leetcode.com/problems/word-break/

Time Complexity: O(n³) where n is the length of string s
Space Complexity: O(n + m) where n is the length of string s and m is the number of words in wordDict
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = [None] * len(s)

        def dfs(i):
            if i == len(s):
                return True
            if memo[i] == None:
                memo[i] = False
                word = ""
                for j in range(i, len(s)):
                    word += s[j]
                    if word in wordSet and dfs(j + 1):
                        memo[i] = True
                        break
            return memo[i]

        return dfs(0)
