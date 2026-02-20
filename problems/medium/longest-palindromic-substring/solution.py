"""
Problem: Longest Palindromic Substring
Difficulty: Medium
URL: https://leetcode.com/problems/longest-palindromic-substring/

Time Complexity: O(n²)
Space Complexity: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r

        start = end = 0
        for i in range(len(s)):
            # odd length
            l, r = getPalindrome(i, i)
            if r - l > end - start:
                start, end = l, r

            # even length
            l, r = getPalindrome(i, i + 1)
            if r - l > end - start:
                start, end = l, r

        return s[start:end]
