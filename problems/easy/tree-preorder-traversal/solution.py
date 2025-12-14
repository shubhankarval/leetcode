"""
Problem: Binary Tree Preorder Traversal
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

Time Complexity: O(n) - n is the number of nodes in the tree
Space Complexity: O(h) - h is the height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def traverse(node: Optional[TreeNode]):
            if node:
                lst.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(root)
        return lst
