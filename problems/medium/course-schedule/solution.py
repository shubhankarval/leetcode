"""
Problem: Course Schedule
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule/

Time Complexity: O(V + E * V) ≈ O(E * V) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for graph maps, queue and visited set
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = defaultdict(list)
        for course, prereq in prerequisites:
            courseToPre[course].append(prereq)

        path = [False] * numCourses

        # check if cycle exists in graph
        def dfs(course):
            if path[course]:
                return True
            path[course] = True

            if course in courseToPre:
                for prereq in courseToPre[course]:
                    if dfs(prereq):
                        return True

            path[course] = False
            return False

        for course in range(numCourses):
            if dfs(course):
                return False

        return True
