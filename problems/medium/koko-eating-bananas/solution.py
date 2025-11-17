"""
Problem: Koko Eating Bananas
Difficulty: Medium
URL: https://leetcode.com/problems/koko-eating-bananas/

Time Complexity: O(nlogm) where n is the number of piles and m is the maximum bananas in a pile
Space Complexity: O(1)
"""

from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        s1, s2 = 1, max(piles)
        speed = 0
        while s1 <= s2:
            currSpeed = (s1 + s2) // 2
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile / currSpeed)

            if currHours <= hours:
                s2 = currSpeed - 1  # decrease speed to increase time
                speed = currSpeed
            else:
                s1 = currSpeed + 1  # increase speed to decrease time

        return speed
