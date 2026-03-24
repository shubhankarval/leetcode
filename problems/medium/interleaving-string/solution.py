"""
Problem: Interleaving String
Difficulty: Medium
URL: https://leetcode.com/problems/interleaving-string/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m and n are the lengths of s1 and s2 respectively.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1), len(s2), len(s3)
        if x + y != z:
            return False
        dp = {}

        def dfs(i, j, k):
            if k == z:
                return True
            if (i, j, k) not in dp:
                res = False
                if i < x and s1[i] == s3[k]:
                    res = dfs(i + 1, j, k + 1)
                if not res and j < y and s2[j] == s3[k]:
                    res = dfs(i, j + 1, k + 1)
                dp[(i, j, k)] = res
            return dp[(i, j, k)]

        return dfs(0, 0, 0)
