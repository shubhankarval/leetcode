"""
Problem: Word Ladder
Difficulty: Hard
URL: https://leetcode.com/problems/word-ladder/

Time Complexity: O(n! * L) wghere n is number of words in wordList and L is length of each word
Space Complexity: O(n) for path dictionary and recursion stack
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

        def dfs(currWord, cnt):
            if currWord == endWord:
                return cnt

            path[currWord] = 1
            minCnt = maxCnt
            for word in wordList:
                if not path[word]:
                    # compare currword with word, if only 1 diff then dfs to it
                    i = diff = 0
                    while diff <= 1 and i < len(word):
                        if word[i] != currWord[i]:
                            diff += 1
                        i += 1
                    if diff == 1:
                        minCnt = min(dfs(word, cnt + 1), minCnt)

            path[currWord] = 0
            return minCnt

        cnt = dfs(beginWord, 1)
        return cnt if cnt < maxCnt else 0
