"""
Problem: Hand of Straights
Difficulty: Medium
URL: https://leetcode.com/problems/hand-of-straights/

Time Complexity: O(mlogm) where m = number of unique cards
Space Complexity: O(m)
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card]:
                for i in range(card + 1, card + groupSize):
                    if not count[i] or count[i] < count[card]:
                        return False
                    count[i] -= count[card]

        return True
