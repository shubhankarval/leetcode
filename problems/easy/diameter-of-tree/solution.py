"""
Problem: Diameter of Binary Tree
Difficulty: Easy
URL: https://leetcode.com/problems/diameter-of-binary-tree/

Time Complexity: O(n) - n is the number of nodes in the tree
Space Complexity: O(h) - h is the height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            leftNodes = dfs(node.left)
            rightNodes = dfs(node.right)
            diameter = max(diameter, leftNodes + rightNodes)
            return 1 + max(leftNodes, rightNodes)

        dfs(root)
        return diameter
