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
        words = set(wordDict)

        # can string starting from index i be resolved using wordDict?
        dp = [True] * len(s)

        def dfs(i):
            if i == len(s):
                return True

            if dp[i]:
                word = ""
                for j in range(i, len(s)):
                    word += s[j]
                    if word in words:
                        if dfs(j + 1):
                            return True
            dp[i] = False
            return dp[i]

        return dfs(0)
