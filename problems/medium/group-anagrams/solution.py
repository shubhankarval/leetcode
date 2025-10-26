"""
Problem: Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

Time Complexity: O(n * m log m) where n is number of strings, m is max length
Space Complexity: O(n * m)
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal approach using sorted string as key.

        Anagrams will have the same sorted string representation.

        Time Complexity: O(n * m log m) - sorting each string
        Space Complexity: O(n * m) - storing all strings in hash map
        """
        tracker = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            tracker[sorted_s].append(s)
        return list(tracker.values())
