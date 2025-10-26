"""
Problem: Top K Frequent Elements
Difficulty: Medium
URL: https://leetcode.com/problems/top-k-frequent-elements/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket sort approach using frequency as bucket index.

        Time Complexity: O(n) - linear time
        Space Complexity: O(n) - for frequency map and buckets
        """
        frq = {}
        for num, cnt in Counter(nums).items():
            if cnt not in frq:
                frq[cnt] = []
            frq[cnt].append(num)

        ans = []
        for cnt in range(len(nums), 0, -1):
            if cnt in frq:
                ans.extend(frq[cnt])
                if len(ans) >= k:
                    return ans[:k]

        return ans[:k]

    def topKFrequentSorting(self, nums: List[int], k: int) -> List[int]:
        """
        One-liner using sorting approach.

        Time Complexity: O(n log n) - due to sorting
        Space Complexity: O(n) - for counter and sorted list
        """
        return list(
            map(
                lambda x: x[0],
                sorted(Counter(nums).items(), key=lambda y: y[1], reverse=True)[:k],
            )
        )
