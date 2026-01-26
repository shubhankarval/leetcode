"""
Problem: Course Schedule
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule/

Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for adjacency list, path and recursion stack
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseToPre[course].append(prereq)

        path = [False] * numCourses

        # check if cycle exists in graph
        def dfs(course):
            if path[course]:
                return True
            if not courseToPre[course]:
                return False
            path[course] = True

            for prereq in courseToPre[course]:
                if dfs(prereq):
                    return True

            path[course] = False
            courseToPre[course] = []
            return False

        for course in range(numCourses):
            if dfs(course):
                return False

        return True
