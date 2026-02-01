"""
Problem: Word Ladder
Difficulty: Hard
URL: https://leetcode.com/problems/word-ladder/

Time Complexity: O(N * L²) where N is the number of words and L is the length of each word.
Space Complexity: O(N * L²) for the adjacency map and O(N * L) for the queue and visited set.
"""

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjMap = dict.fromkeys(wordList, [])
        for word in wordList:
            adjMap[word] = self.addAdjacentWords(word, adjMap)
        if endWord not in adjMap:
            return 0
        if beginWord not in adjMap:
            adjMap[beginWord] = self.addAdjacentWords(beginWord, adjMap)

        queue = deque([[beginWord, 1]])  # word, cnt
        visited = set([beginWord])

        while queue:
            currWord, cnt = queue.popleft()
            if currWord == endWord:
                return cnt
            for word in adjMap[currWord]:
                if word not in visited:
                    queue.append([word, cnt + 1])
                    visited.add(word)

        return 0

    def addAdjacentWords(self, word, adjMap):
        words = []
        letters = "qwertyuiopasdfghjklzxcvbnm"

        for i, ch in enumerate(word):
            pre, suf = word[:i], word[i + 1 :]
            for letter in letters:
                if ch != letter:
                    adjWord = pre + letter + suf
                    if adjWord in adjMap:
                        words.append(adjWord)
        return words
