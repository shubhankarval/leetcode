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

from collections import Counter, defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-cnt for cnt in Counter(tasks).values()]
        heapq.heapify(heap)
        cooldown = defaultdict(list)  # cycle -> list of tasks
        cycle = 0

        while len(heap) or len(cooldown):
            if cycle in cooldown:
                for task in cooldown[cycle]:
                    heapq.heappush(heap, task)
                del cooldown[cycle]

            if not len(heap):
                cycle += 1
                continue

            task = heapq.heappop(heap)
            task += 1
            if task:
                cooldown[cycle + n + 1].append(task)

            cycle += 1

        return cycle
