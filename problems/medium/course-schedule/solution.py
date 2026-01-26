"""
Problem: Course Schedule
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule/

Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for adjacency list, path, visited and recursion stack
"""

from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = defaultdict(list)
        for course, prereq in prerequisites:
            courseToPre[course].append(prereq)

        path, visited = [False] * numCourses, [False] * numCourses

        # check if cycle exists in graph
        def dfs(course):
            if path[course]:
                return True
            if visited[course]:
                return False
            path[course] = True
            visited[course] = True

            if course in courseToPre:
                for prereq in courseToPre[course]:
                    if dfs(prereq):
                        return True

            path[course] = False
            return False

        for course in range(numCourses):
            if not visited[course] and dfs(course):
                return False

        return True
