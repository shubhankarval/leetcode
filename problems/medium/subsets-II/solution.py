"""
Problem: Subsets II
Difficulty: Medium
URL: https://leetcode.com/problems/subsets-ii/

Time Complexity: O(n * 2^n) where n is the size of the input array
Space Complexity: O(n) where n is the recursion depth
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(lst, i):
            res.append(lst.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                lst.append(nums[j])
                dfs(lst, j + 1)
                lst.pop()

        dfs([], 0)
        return res
