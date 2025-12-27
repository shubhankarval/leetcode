"""
Problem: Word Search
Difficulty: Medium
URL: https://leetcode.com/problems/word-search/

Time Complexity: Time: O(m * n * 4^L) where m is number of rows, n is number of columns, and L is the length of the word
Space Complexity: O(L) where L is the length of the word
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

                s.add((r, c))
                for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if dfs(row, col, i, s):
                        return True
                s.remove((r, c))

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True

        return False
