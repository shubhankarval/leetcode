"""
Problem: Valid Binary Search Tree
Difficulty: Medium
URL: https://leetcode.com/problems/validate-binary-search-tree/

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lesser, greater):
            if not node:
                return True
            if node.val >= lesser or node.val <= greater:
                return False
            return dfs(node.left, node.val, greater) and dfs(
                node.right, lesser, node.val
            )

        return dfs(root, float("inf"), float("-inf"))
