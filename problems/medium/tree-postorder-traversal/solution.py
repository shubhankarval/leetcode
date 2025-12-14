"""
Problem: Binary Tree Postorder Traversal
Difficulty: Medium
URL: https://leetcode.com/problems/binary-tree-postorder-traversal/

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lst = []

        def traverse(node: Optional[TreeNode]):
            if node:
                traverse(node.left)
                traverse(node.right)
                lst.append(node.val)
        
        traverse(root)
        return lst