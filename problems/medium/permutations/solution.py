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

        def dfs(lst, pick):
            if len(lst) == len(nums):
                res.append(lst.copy())
                return
            for i in range(len(nums)):
                if not pick[i]:
                    lst.append(nums[i])
                    pick[i] = True
                    dfs(lst, pick)
                    lst.pop()
                    pick[i] = False

        dfs([], [False] * len(nums))
        return res
