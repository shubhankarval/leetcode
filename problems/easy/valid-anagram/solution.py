"""
Problem: Valid Anagram
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
