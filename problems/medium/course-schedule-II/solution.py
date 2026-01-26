"""
Problem: Course Schedule II
Difficulty: Medium
URL: https://leetcode.com/problems/course-schedule-ii/

Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
Space Complexity: O(V + E) for adjacency list, indegree array and queue
"""

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses  # no. of incoming edges
        adjList = [[] for _ in range(numCourses)]  # prereq[i] = [courses]
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        finishedCourses = []
        while queue:
            prereq = queue.popleft()
            finishedCourses.append(prereq)
            for course in adjList[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return finishedCourses if len(finishedCourses) == numCourses else []
