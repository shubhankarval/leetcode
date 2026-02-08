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
                if len(sub) > len(res) and self.isPalindrome(sub):
                    res = sub

        return res

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
