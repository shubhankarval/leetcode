"""
Problem: Merge Triplets to Form Target
Difficulty: Medium
URL: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-1, -1, -1]

        for triplet in triplets:
            goToNext = False
            for i in range(3):
                if triplet[i] > target[i]:
                    goToNext = True
                    break
            if goToNext:
                continue

            for i in range(3):
                res[i] = max(res[i], triplet[i])
            if res == target:
                return True

        return False
