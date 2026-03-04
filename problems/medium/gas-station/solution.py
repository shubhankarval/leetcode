"""
Problem: Gas Station
Difficulty: Medium
URL: https://leetcode.com/problems/gas-station/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's mathematically impossible
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start_idx = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]

            # If we run out of gas, this start_idx (and all before it) is invalid
            if total_tank < 0:
                start_idx = i + 1
                total_tank = 0

        return start_idx
