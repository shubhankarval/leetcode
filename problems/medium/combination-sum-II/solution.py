"""
Problem: Combination Sum II
Difficulty: Medium
URL: https://leetcode.com/problems/combination-sum-ii/

Time Complexity: O(2^n) where n is the number of candidates
Space Complexity: O(n) for the recursion stack
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(lst, total, i):
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] >= target:
                    if total + candidates[j] == target:
                        res.append(lst + [candidates[j]])
                    return

                lst.append(candidates[j])
                dfs(lst, total + candidates[j], j + 1)
                lst.pop()

        dfs([], 0, 0)
        return res
