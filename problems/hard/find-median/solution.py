"""
Problem: Find Median From Data Stream
Difficulty: Hard
URL: https://leetcode.com/problems/find-median-from-data-stream/

Time Complexity: O(log n) for findMedian(), O(1) for addNum()
Space Complexity: O(n)

where n is the number of elements in the data stream.
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.lesser = []  # -nums from first half of list (maxHeap)
        self.greater = []  # nums from second half of list (minHeap)

    def addNum(self, num: int) -> None:
        if len(self.greater) and num > self.greater[0]:
            heapq.heappush(self.greater, num)
        else:
            heapq.heappush(self.lesser, -num)

        if len(self.lesser) - len(self.greater) > 1:
            num = -heapq.heappop(self.lesser)
            heapq.heappush(self.greater, num)
        elif len(self.greater) - len(self.lesser) > 1:
            num = heapq.heappop(self.greater)
            heapq.heappush(self.lesser, -num)

    def findMedian(self) -> float:
        if len(self.lesser) > len(self.greater):
            return -self.lesser[0]
        elif len(self.greater) > len(self.lesser):
            return self.greater[0]
        return (-self.lesser[0] + self.greater[0]) / 2
