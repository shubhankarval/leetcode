"""
Problem: Balanced Binary Tree
Difficulty: Easy
URL: https://leetcode.com/problems/balanced-binary-tree/

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            leftNodes = dfs(node.left)
            if leftNodes == -1:
                return -1

            rightNodes = dfs(node.right)
            if rightNodes == -1 or abs(leftNodes - rightNodes) > 1:
                return -1

            return 1 + max(leftNodes, rightNodes)

        return dfs(root) != -1
