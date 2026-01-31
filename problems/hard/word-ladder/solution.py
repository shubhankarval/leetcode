"""
Problem: Word Ladder
Difficulty: Hard
URL: https://leetcode.com/problems/word-ladder/

Time Complexity: O(n²L + n!) ≈ O(n!) where n is number of words in wordList and L is length of each word
Space Complexity: O(n²) for wordJump & path dictionaries and recursion stack
"""

"""
Intuition:
compare each word with all other words, see where it can jump to
run dfs starting from beginWord
if not possible to reach endWord return maxCnt
else return min count 
"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        path = {word: 0 for word in wordList}
        if endWord not in path:
            return 0
        path[beginWord] = 0
        maxCnt = len(wordList) + 2  # beyond possible count of words

        wordJump = {}
        for i, word in enumerate(wordList):
            wordJump[word] = self.compareWords(word, i, wordList)
        if beginWord not in wordJump:
            wordJump[beginWord] = self.compareWords(beginWord, -1, wordList)

        def dfs(currWord, cnt):
            if currWord == endWord:
                return cnt
            path[currWord] = 1
            minCnt = maxCnt

            for word in wordJump[currWord]:
                if not path[word]:
                    minCnt = min(dfs(word, cnt + 1), minCnt)

            path[currWord] = 0
            return minCnt

        cnt = dfs(beginWord, 1)
        return cnt if cnt < maxCnt else 0

    def compareWords(self, currWord: str, currIdx: int, wordList: str):
        jumpWords = []
        for i, word in enumerate(wordList):
            if i != currIdx:
                j = diff = 0
                while diff <= 1 and j < len(word):
                    if word[j] != currWord[j]:
                        diff += 1
                    j += 1
                if diff == 1:
                    jumpWords.append(word)
        return jumpWords
