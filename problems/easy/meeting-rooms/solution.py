"""
Problem: Meeting Rooms
Difficulty: Easy
URL: https://leetcode.com/problems/meeting-rooms/

Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(lambda x: (x.start, x.end))

        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False

        return True
