"""
Problem: Alien Dictionary
Difficulty: Hard
URL: https://neetcode.io/problems/foreign-dictionary/

Time Complexity: O(N + V + E)
Space Complexity: O(V + E)
- where N = total number of characters in all words
        V = number of unique characters
        E = number of edges in the graph
"""

from typing import List
from collections import deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjMap = {ch: [] for w in words for ch in w}
        inDeg = {ch: 0 for ch in adjMap}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            l1, l2 = len(w1), len(w2)
            added = False

            for j in range(min(l1, l2)):
                c1, c2 = w1[j], w2[j]
                if not added and c1 != c2:
                    adjMap[c1].append(c2)
                    inDeg[c2] += 1
                    added = True
                    break

            if not added and l1 > l2:
                return ""

        res = []
        queue = deque([ch for ch in inDeg if inDeg[ch] == 0])

        while queue:
            ch = queue.popleft()
            res.append(ch)

            for adjCh in adjMap[ch]:
                inDeg[adjCh] -= 1
                if inDeg[adjCh] == 0:
                    queue.append(adjCh)

        return "".join(res) if len(res) == len(adjMap) else ""
