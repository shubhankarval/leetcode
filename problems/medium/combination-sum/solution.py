"""
Problem: Combination Sum
Difficulty: Medium
URL: https://leetcode.com/problems/combination-sum/

Time Complexity: O(n ^ (t/m))
Space Complexity: O(t/m)

where - n is the length of nums
      - t is the target
      - m is the minimum value in nums
"""

"""
Intuition:
Sort list
Recurse through array
Stop the moment sum exceeds the target
Start with empty array
Choose whether to select num or not
"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(lst, total, i):
            if total > target:
                return False
            if total == target:
                res.append(lst)
                return False
            if i < len(nums):
                if dfs(lst + [nums[i]], total + nums[i], i):
                    dfs(lst, total, i + 1)
            return True

        dfs([], 0, 0)
        return res
