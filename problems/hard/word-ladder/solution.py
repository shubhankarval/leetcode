"""
Problem: Word Ladder
Difficulty: Hard
URL: https://leetcode.com/problems/word-ladder/

Time Complexity: O(N * L²) where N is the number of words and L is the length of each word.
Space Complexity: O(N * L) for the adjacency map, queues, and visited dictionaries.
"""

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordSet.add(beginWord)

        q1, q2 = deque([beginWord]), deque([endWord])
        fromBegin, fromEnd = {beginWord: 1}, {endWord: 1}

        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                fromBegin, fromEnd = fromEnd, fromBegin

            size = len(q1)
            for _ in range(size):
                currWord = q1.popleft()
                dist = fromBegin[currWord]

                for word in self.getAdjacentWords(currWord, wordSet):
                    if word in fromEnd:
                        return dist + fromEnd[word]
                    if word not in fromBegin:
                        fromBegin[word] = dist + 1
                        q1.append(word)

        return 0

    def getAdjacentWords(self, word, wordSet):
        words = []
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for letter in letters:
                if word[i] != letter:
                    adjWord = word[:i] + letter + word[i + 1 :]
                    if adjWord in wordSet:
                        words.append(adjWord)
        return words
