"""
Problem: Same Binary Tree
Difficulty: Easy
URL: https://leetcode.com/problems/same-tree/

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if not n1 and not n2:
                return True
            if n1 and n2 and n1.val != n2.val:
                return dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
            return False

        return dfs(p, q)
