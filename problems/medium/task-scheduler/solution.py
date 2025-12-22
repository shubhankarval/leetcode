"""
Problem: Task Scheduler
Difficulty: Medium
URL: https://leetcode.com/problems/task-scheduler/

Time Complexity: O(n log k) where n is number of tasks, k is number of unique tasks
Space Complexity: O(k) where k is number of unique tasks
here, k ≤ 26
"""

"""
Intuition:
need count of each task, start task with highest count
track next avlbl slot for task, update it when task finishes
if count of task reaches 0, remove task
"""

from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)
        cooldown = deque([])  # [cycle, task]
        cycle = 0

        while len(heap) or len(cooldown):
            while len(cooldown) and cycle == cooldown[0][0]:
                heapq.heappush(heap, cooldown.popleft()[1])

            if not len(heap):
                cycle = cooldown[0][0]
                continue

            task = heapq.heappop(heap)
            task += 1
            if task:
                cooldown.append([cycle + n + 1, task])

            cycle += 1

        return cycle
