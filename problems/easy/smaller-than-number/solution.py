"""
Problem: How many numbers are smaller than the current number?
Difficulty: Easy
URL: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

"""
for each number:
ans = ans of prev number + count of prev num
"""

from typing import List
from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = {}
        for i, n in enumerate(sorted(nums)):
            if n not in res:
                res[n] = i
        return [res[n] for n in nums]

    """
    Min-max approach
    Time Complexity: O(n + k) where n is the length of nums and k is the range of numbers (max - min)
    Space Complexity: O(n) in worst case if all numbers are unique
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        minN, maxN = min(nums), max(nums)

        res, prev = {minN: 0}, minN
        for n in range(minN + 1, maxN + 1):
            if n in cnt:
                res[n] = res[prev] + cnt[prev]
                prev = n

        return [res[n] for n in nums]
