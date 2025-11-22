"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time Complexity: O(n) where n is the length of the string s
Space Complexity: O(m) where m is the number of unique characters in the string s
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, chars = 0, {}
        l = r = 0
        while r < len(s):
            if s[r] in chars:
                idx = chars[s[r]]
                if idx < l:
                    del chars[s[r]]
                else:
                    length = max(length, r - l)
                    l = idx + 1
            chars[s[r]] = r
            r += 1
        return max(length, r - l)
