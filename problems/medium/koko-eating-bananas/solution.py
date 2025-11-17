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
            currSpeed = s1 + (s2 - s1) // 2
            currHours = self.getHours(piles, currSpeed)
            if currHours > hours:
                s1 = currSpeed + 1  # increase speed to decrease time
            elif currHours < hours:
                s2 = currSpeed - 1  # decrease speed to increase time
                speed = currSpeed
            else:
                s2 = currSpeed - 1  # continue search to find min speed
                speed = currSpeed
        return speed

    def getHours(self, piles: List[int], k: int) -> int:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)
        return hours
