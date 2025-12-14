"""
Problem: Binary Tree Inorder Traversal
Difficulty: Easy
URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def traverse(node: Optional[TreeNode]):
            if node:
                traverse(node.left)
                lst.append(node.val)
                traverse(node.right)

        traverse(root)
        return lst
