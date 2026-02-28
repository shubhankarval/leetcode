"""
Problem: Meeting Rooms II
Difficulty: Easy
URL: https://leetcode.com/problems/meeting-rooms-ii/

Time Complexity: O(n²)
Space Complexity: O(n)
"""

from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        rooms = []

        for interval in intervals:
            roomFound = False
            for i in range(len(rooms)):
                if rooms[i] <= interval.start:
                    rooms[i] = interval.end
                    roomFound = True
                    break
            if not roomFound:
                rooms.append(interval.end)

        return len(rooms)
