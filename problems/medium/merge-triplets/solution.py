"""
Problem: Merge Triplets to Form Target
Difficulty: Medium
URL: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        res = [-1, -1, -1]

        for triplet in triplets:
            goToNext = False
            for i in range(3):
                if triplet[i] > target[i]:
                    if i == 0:
                        return False
                    goToNext = True
                    break
            if goToNext:
                continue

            for i in range(3):
                res[i] = max(res[i], triplet[i])
            if res == target:
                return True

        return False
