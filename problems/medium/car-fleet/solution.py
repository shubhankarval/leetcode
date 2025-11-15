"""
Problem: Car Fleet
Difficulty: Medium
URL: https://leetcode.com/problems/car-fleet/

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed), reverse=True)
        fleets = 1
        nextTime = (target - paired[0][0]) / paired[0][1]

        for i in range(1, len(paired)):
            currTime = (target - paired[i][0]) / paired[i][1]
            if currTime > nextTime:
                nextTime = currTime
                fleets += 1

        return fleets
