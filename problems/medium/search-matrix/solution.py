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
        row = -1
        t, b = 0, len(matrix) - 1
        while t <= b:
            m = t + (b - t) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                row = m
                break
            elif target > matrix[m][-1]:
                t = m + 1
            else:
                b = m - 1
        if row != -1:
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                m = l + (r - l) // 2
                if target > matrix[row][m]:
                    l = m + 1
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    return True

        return False
