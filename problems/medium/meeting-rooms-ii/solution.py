"""
Problem: Meeting Rooms II
Difficulty: Easy
URL: https://neetcode.io/problems/meeting-schedule-ii

Time Complexity: O(nlogn)
Space Complexity: O(n)
"""

from typing import List
import heapq


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = [intervals[0].end]

        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms[0]:
                heapq.hep(rooms)
            heapq.heappush(rooms, intervals[i].end)

        return len(rooms)
