"""
Problem: Counting Bits
Difficulty: Easy
URL: https://leetcode.com/problems/counting-bits/

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            cnt = 0
            while i:
                if i & 1:
                    cnt += 1
                i >>= 1
            res.append(cnt)
        return res
