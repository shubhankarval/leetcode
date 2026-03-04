"""
Problem: Gas Station
Difficulty: Medium
URL: https://leetcode.com/problems/gas-station/

Time Complexity: O(n²)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            j, currGas = i, gas[i]

            while currGas - cost[j] >= 0:
                currGas -= cost[j]
                j = j + 1 if j < len(gas) - 1 else 0
                if j == i:
                    return i
                currGas += gas[j]

        return -1
