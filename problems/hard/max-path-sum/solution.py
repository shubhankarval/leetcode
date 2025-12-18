"""
Problem: Binary Tree Maximum Path Sum
Difficulty: Hard
URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree due to recursion stack
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            maxL = dfs(node.left)
            maxR = dfs(node.right)
            maxSum = max(maxSum, node.val + maxL + maxR)

            return max(node.val + max(maxL, maxR), 0)

        dfs(root)
        return maxSum
