"""
Problem: Car Fleet
Difficulty: Medium
URL: https://leetcode.com/problems/car-fleet/

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = sorted(zip(position, speed))
        stack = []

        for pos, speed in paired:
            time = (target - pos) / speed
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)

        return len(stack)
