"""
Problem: Word Search
Difficulty: Medium
URL: https://leetcode.com/problems/word-search/

Time Complexity: Time: O(m * n * 4^L) where m is number of rows, n is number of columns, and L is the length of the word
Space Complexity: O(L²) where L is the length of the word
"""

"""
Recurse thru matrix
dfs with params r, c, i
do a dfs OR condition/use a global var to return result
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i, s):
            if not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in s:
                return False
            if board[r][c] == word[i]:
                i += 1
                if i == len(word):
                    return True
                s = s | {(r, c)}
                return (
                    dfs(r + 1, c, i, s)
                    or dfs(r - 1, c, i, s)
                    or dfs(r, c + 1, i, s)
                    or dfs(r, c - 1, i, s)
                )
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True

        return False
