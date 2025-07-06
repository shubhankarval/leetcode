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


def test_solution():
    solution = Solution()

    # Test case 1: Basic case
    result1 = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
    expected1 = [1, 2]  # Can be in any order
    assert set(result1) == set(expected1), f"Expected {expected1}, got {result1}"
    assert len(result1) == 2, f"Expected length 2, got {len(result1)}"

    # Test case 2: Single element
    result2 = solution.topKFrequent([1], 1)
    assert result2 == [1], f"Expected [1], got {result2}"

    # Test case 3: All unique elements
    result3 = solution.topKFrequent([1, 2, 3, 4, 5], 3)
    assert len(result3) == 3, f"Expected length 3, got {len(result3)}"

    # Test case 4: k equals array length
    result4 = solution.topKFrequent([1, 2], 2)
    assert set(result4) == {1, 2}, f"Expected {{1, 2}}, got {set(result4)}"

    # Test all alternative approaches
    result_sort = solution.topKFrequentSorting([1, 1, 1, 2, 2, 3], 2)
    assert set(result_sort) == {1, 2}, "Sorting approach failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
