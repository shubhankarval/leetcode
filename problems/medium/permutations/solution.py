"""
Problem: Permutations
Difficulty: Medium
URL: https://leetcode.com/problems/permutations/

Time Complexity: O(n * n!) where n is the size of the input array
Space Complexity: O(n) where n is the recursion depth
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(lst, s):
            if len(lst) == len(nums):
                res.append(lst.copy())
                return
            for i in range(len(nums)):
                if nums[i] not in s:
                    lst.append(nums[i])
                    s.add(nums[i])
                    dfs(lst, s)
                    lst.pop()
                    s.remove(nums[i])

        dfs([], set())
        return res
