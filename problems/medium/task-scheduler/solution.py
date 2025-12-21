"""
Problem: Task Scheduler
Difficulty: Medium
URL: https://leetcode.com/problems/task-scheduler/

Time Complexity: O(n + k log k) where n is number of tasks, k is number of unique tasks
Space Complexity: O(k) where k is number of unique tasks
here, k <= 26
"""

"""
Intuition:
need count of each task, start task with highest count
track next avlbl slot for task, update it when task finishes
if count of task reaches 0, remove task
"""

from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = [[-cnt, 0] for cnt in Counter(tasks).values()]
        heapq.heapify(pq)
        cycle = 0

        while len(pq):
            removed = []
            while len(pq) and pq[0][1] > cycle:
                removed.append(heapq.heappop(pq))

            if not len(pq):
                pq = removed
                cycle += 1
                continue

            task = heapq.heappop(pq)
            task[0] += 1
            if task[0]:
                task[1] = cycle + n + 1
                heapq.heappush(pq, task)

            pq = removed + pq
            cycle += 1

        return cycle
