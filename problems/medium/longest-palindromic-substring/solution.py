"""
Problem: Longest Palindromic Substring
Difficulty: Medium
URL: https://leetcode.com/problems/longest-palindromic-substring/

Time Complexity: O(n³)
Space Complexity: O(n)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        for i in range(len(s)):
            sub = s[i]
            for j in range(i + 1, len(s)):
                sub += s[j]
                if len(sub) > len(res) and sub == sub[::-1]:
                    res = sub

        return res
