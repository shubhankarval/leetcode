"""
Problem: Hand of Straights
Difficulty: Medium
URL: https://leetcode.com/problems/hand-of-straights/

Time Complexity: O(nlogn + m*k)
Space Complexity: O(m)
- where n = number of cards
        m = number of unique cards
        k = groupSize
"""

from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        cards = sorted(Counter.keys())

        for i in range(len(cards)):
            currCount = count[cards[i]]
            del count[cards[i]]
            if currCount == 0:
                continue

            if i + groupSize > len(cards):
                return False

            for j in range(i + 1, i + groupSize):
                if cards[j - 1] + 1 != cards[j] or count[cards[j]] < currCount:
                    return False
                count[cards[j]] -= currCount

        return len(count) == 0
