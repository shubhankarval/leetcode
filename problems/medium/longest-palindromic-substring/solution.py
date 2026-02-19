"""
Problem: Longest Palindromic Substring
Difficulty: Medium
URL: https://leetcode.com/problems/longest-palindromic-substring/

Time Complexity: O(n³)
Space Complexity: O(n)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            j = i + len(res)
            if j >= len(s):
                break
            word = s[i:j]
            for k in range(j, len(s)):
                word += s[k]
                if self.isPalindrome(word):
                    res = word
        return res

    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
