"""
Problem: Time Based Key-Value Store
Difficulty: Medium
URL: https://leetcode.com/problems/time-based-key-value-store/

Time Complexity: O(log n) for get, O(1) for set
Space Complexity: O(m * n) where m is number of keys and n is number of values per key
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        values = self.timeMap[key]
        l, r = 0, len(values) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            ts, val = values[m]
            if ts < timestamp:
                l = m + 1
                res = val
            elif ts > timestamp:
                r = m - 1
            else:
                return val
        return res
