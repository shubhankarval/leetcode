"""
Problem: Binary Tree Level Order Traversal
Difficulty: Medium
URL: https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, level):
            if node:
                if level <= len(res) - 1:
                    res[level].append(node.val)
                else:
                    res.append([node.val])

                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return res
