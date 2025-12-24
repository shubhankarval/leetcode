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
            if i < len(nums):
                dfs(lst, i + 1)
                dfs(lst + [nums[i]], i + 1)
            else:
                res.append(lst)

        dfs([], 0)
        return res
