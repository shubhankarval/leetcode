"""
Problem: Search a 2D Matrix
Difficulty: Medium
URL: https://leetcode.com/problems/search-a-2d-matrix/

Time Complexity: O(log(m * n)) where m and n are dimensions of the matrix
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // cols, m % cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
