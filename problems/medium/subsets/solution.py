"""
Problem: Subsets
Difficulty: Medium
URL: https://leetcode.com/problems/subsets/

Time Complexity: O(n * 2^n) where n is the size of the input array
Space Complexity: O(n) where n is the recursion depth
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(lst, i):
            res.append(lst.copy())
            for j in range(i, len(nums)):
                lst.append(nums[j])
                dfs(lst, j + 1)
                lst.pop()

        dfs([], 0)
        return res
