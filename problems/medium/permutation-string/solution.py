"""
Problem: Permutation in String
Difficulty: Medium
URL: https://leetcode.com/problems/permutation-in-string/

Time Complexity: O(n * m) where n is the len(s2) and m is len(s1)
Space Complexity: O(26) = O(1) since the character set is fixed
"""

"""
Intuition:
Create freq map for s1
from each element in s2 go upto len(s1) elems from it
create freq hash maps for that substring
if hash maps are same, then return True, otherwise continue
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = Counter(s1)
        l = r = 0
        while l < len(s2):
            chars2 = {}
            length = 0
            while r < len(s2) and s2[r] in chars and length < len(s1):
                chars2[s2[r]] = chars2.get(s2[r], 0) + 1
                r += 1
                length += 1
            if length == len(s1):
                if chars == chars2:
                    return True
                else:
                    l += 1
                    r = l
            else:
                r += 1
                l = r
        return False
