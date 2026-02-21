"""
Problem: Word Break
Difficulty: Medium
URL: https://leetcode.com/problems/word-break/

Time Complexity: O(n * m * t)
Space Complexity: O(n)
- where n = length of string s,
        m = number of words in wordDict,
        t = maximum length of a word in wordDict
"""

from typing import List


class Solution:
    # DP Top-Down (Optimimal)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [None] * (len(s) + 1)
        memo[len(s)] = True

        def dfs(i):
            if memo[i] == None:
                memo[i] = False
                for word in wordDict:
                    wordEnd = i + len(word)
                    if wordEnd <= len(s) and s[i:wordEnd] == word and dfs(wordEnd):
                        memo[i] = True
                        break
            return memo[i]

        return dfs(0)

    # DP Top-Down (Suboptimal)
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
