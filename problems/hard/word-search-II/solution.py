"""
Problem: Word Search II
Difficulty: Hard
URL: https://leetcode.com/problems/word-search-ii/

Time Complexity: O(W * P * 4^L)
Space Complexity: O(m * n + L²)

where - W is the number of words in the input list
      - P is the average length of the words
      - L is the maximum length of the words
"""

from collections import defaultdict


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pos = defaultdict(list)  # ch -> list of (r, c)
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                pos[board[r][c]].append((r, c))

        def dfs(r, c, seen, curr, target):
            if not 0 <= r < rows or not 0 <= c < cols or (r, c) in seen:
                return False
            curr += board[r][c]
            seen.add((r, c))
            if len(curr) == len(target):
                return curr == target
            for row, col in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]:
                if dfs(row, col, seen.copy(), curr, target):
                    return True
            return False

        res = []
        for word in words:
            if word[0] in pos:
                for r, c in pos[word[0]]:
                    if dfs(r, c, set(), "", word):
                        res.append(word)
                        break

        return res
