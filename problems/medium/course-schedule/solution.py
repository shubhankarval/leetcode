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
        courseToPre = defaultdict(set)
        preToCourse = defaultdict(set)

        for course, prereq in prerequisites:
            courseToPre[course].add(prereq)
            preToCourse[prereq].add(course)

        queue, visited = deque([]), set()
        for num in range(numCourses):
            if num not in courseToPre:
                queue.append(num)
                visited.add(num)

        while queue:
            prereq = queue.popleft()

            for course in preToCourse[prereq]:
                if course not in visited and courseToPre[course].issubset(visited):
                    queue.append(course)
                    visited.add(course)

        return len(visited) == numCourses
