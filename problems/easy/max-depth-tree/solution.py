"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Time Complexity: O(n) - n is the number of nodes in the tree
Space Complexity: O(h) - h is the height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        def traverse(node, depth):
            nonlocal maxDepth  # This allows modifying the outer maxDepth
            if node:
                traverse(node.left, depth + 1)
                traverse(node.right, depth + 1)
                maxDepth = max(maxDepth, depth + 1)

        traverse(root, 0)
        return maxDepth
