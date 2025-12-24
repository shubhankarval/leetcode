"""
Problem: Subsets
Difficulty: Medium
URL: https://leetcode.com/problems/subsets/

Time Complexity: O(n * 2^n)
Space Complexity: O(n * 2^n)

where n is the size of the input array.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(tup, i):
            # print(tup, i, res)
            if tup not in res:
                res.add(tup)
            if i < len(nums):
                dfs(tup, i + 1)
                dfs(tup + (nums[i],), i + 1)

        dfs(tuple(), 0)
        return list(map(lambda x: list(x), list(res)))
