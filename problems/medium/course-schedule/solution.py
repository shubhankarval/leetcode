"""
Problem: Course Schedule
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule/

Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for adjacency list and path/queue
"""

from typing import List
from collections import deque


class Solution:
    # Cycle detection
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

    # Topological sort (Kahn's algorithm)
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses  # no. of incoming edges
        adjList = {i: [] for i in range(numCourses)}  # prereq -> courses

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        coursesFinished = 0
        while queue:
            prereq = queue.popleft()
            coursesFinished += 1
            for course in adjList[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return coursesFinished == numCourses
