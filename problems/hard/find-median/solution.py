"""
Problem: Find Median From Data Stream
Difficulty: Hard
URL: https://leetcode.com/problems/find-median-from-data-stream/

Time Complexity: O(log n) for findMedian(), O(1) for addNum()
Space Complexity: O(n)

where n is the number of elements in the data stream.
"""

from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        self.nums = SortedList([])

    def addNum(self, num: int) -> None:
        self.nums.add(num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:
            return (self.nums[mid] + self.nums[mid - 1]) / 2
        return self.nums[mid]
