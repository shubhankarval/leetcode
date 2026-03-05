"""
Problem: Hand of Straights
Difficulty: Medium
URL: https://leetcode.com/problems/hand-of-straights/

Time Complexity: O(n²)
Space Complexity: O(n)
"""

from collections import deque
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        queue = deque([0])
        visited = set()

        while queue:
            start = end = queue.popleft()
            visited.add(start)
            prev = hand[start]
            size = 1

            for i in range(start + 1, len(hand)):
                if size == groupSize:
                    break
                if i not in visited:
                    if prev == hand[i]:
                        if not queue:
                            queue.append(i)
                    elif prev + 1 != hand[i]:
                        return False
                    else:
                        visited.add(i)
                        prev = hand[i]
                        size += 1
                end = i

            if size != groupSize:
                return False
            if not queue and end != len(hand) - 1:
                queue.append(end + 1)

        return True
