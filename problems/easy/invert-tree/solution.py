"""
Problem: Invert Binary Tree
Difficulty: Easy
URL: https://leetcode.com/problems/invert-binary-tree/

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Intuition:
if node has left go left, if node has right go right
then switch left and right nodes
"""

from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node: Optional[TreeNode]):
            if node:
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
                node.left, node.right = node.right, node.left

        traverse(root)
        return root
