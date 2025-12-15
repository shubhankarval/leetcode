"""
Problem: Binary Tree Right Side View
Difficulty: Medium
URL: https://leetcode.com/problems/binary-tree-right-side-view/

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Intuition:
create algo so that right node at any level will be last to be visited for that lvl
create list for nodes
"""

from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level):
            if node:
                if level == len(res):
                    res.append(node.val)
                else:
                    res[level] = node.val

                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return res
