"""
Problem: Permutation in String
Difficulty: Medium
URL: https://leetcode.com/problems/permutation-in-string/

Time Complexity: O(n) where n is len(s2)
Space Complexity: O(26) = O(1) since the character set is fixed
"""

"""
Intuition:
create freq map of s1
create two pointers l and r
create freq map of s2 of len(s1's freq map) starting from idx 0
if they match return true, if not reduce l's val by 1 and do l+=1, r+=1
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        freq1, freq2 = Counter(s1), Counter(s2[l:r])
        while r < len(s2):
            prevCh, newCh = s2[l], s2[r]
            freq2[newCh] = freq2.get(newCh, 0) + 1
            if freq1 == freq2:
                return True
            freq2[prevCh] -= 1
            if freq2[prevCh] == 0:
                del freq2[prevCh]
            l += 1
            r += 1
        return False
