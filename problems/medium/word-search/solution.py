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

        def dfs(r, c, i):
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or board[r][c] == "#"
                or board[r][c] != word[i]
            ):
                return False

            i += 1
            if i == len(word):
                return True

            board[r][c] = "#"
            res = (
                dfs(r + 1, c, i)
                or dfs(r - 1, c, i)
                or dfs(r, c + 1, i)
                or dfs(r, c - 1, i)
            )
            board[r][c] = word[i - 1]

            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
