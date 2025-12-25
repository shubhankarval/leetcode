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
Start with empty array
Choose whether to select num or not
Stop the moment sum exceeds the target
"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(lst, total, i):
            if total == target:
                res.append(lst.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return

                lst.append(nums[j])
                dfs(lst, total + nums[j], j)
                lst.pop()

        dfs([], 0, 0)
        return res
