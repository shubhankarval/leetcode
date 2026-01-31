"""
Problem: Word Ladder
Difficulty: Hard
URL: https://leetcode.com/problems/word-ladder/

Time Complexity: O(N² * L) where N is the number of words in wordList and L is the length of each word.
Space Complexity: O(N²) for the adjacency map and O(N) for the queue and visited set.
"""

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjMap = {}
        beginIdx = endIdx = -1
        for i, word in enumerate(wordList):
            adjMap[i] = self.addAdjacentNodes(word, i, wordList)
            if word == beginWord:
                beginIdx = i
            elif word == endWord:
                endIdx = i
        if endIdx == -1:
            return 0
        if beginIdx == -1:
            adjMap[beginIdx] = self.addAdjacentNodes(beginWord, beginIdx, wordList)

        queue = deque([[beginIdx, 1]])  # idx, cnt
        visited = set([beginIdx])  # set of indices

        while queue:
            currIdx, cnt = queue.popleft()
            if currIdx == endIdx:
                return cnt
            for i in adjMap[currIdx]:
                if i not in visited:
                    queue.append([i, cnt + 1])
                    visited.add(i)

        return 0

    def addAdjacentNodes(self, currWord, currIdx, wordList):
        wordIndices = []
        for wordIdx, word in enumerate(wordList):
            if wordIdx != currIdx:
                diff = i = 0
                while diff <= 1 and i < len(currWord):
                    if word[i] != currWord[i]:
                        diff += 1
                    i += 1
                if diff == 1:
                    wordIndices.append(wordIdx)
        return wordIndices
