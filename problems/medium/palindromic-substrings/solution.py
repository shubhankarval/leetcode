"""
Problem: Palindromic Substrings
Difficulty: Medium
URL: https://leetcode.com/problems/palindromic-substrings/

Time Complexity: O(n²)
Space Complexity: O(1)
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalindromeCount(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 1
            return cnt

        totalCnt = 0
        for i in range(len(s)):
            # odd and even length
            totalCnt += getPalindromeCount(i, i) + getPalindromeCount(i, i + 1)
        return totalCnt
