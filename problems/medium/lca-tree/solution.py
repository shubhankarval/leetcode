"""
Problem: Lowest Common Ancestor in Binary Search Tree
Difficulty: Medium
URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Time Complexity: O(h) where h is the height of the tree
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
find p & q in tree
if either is not found, 
create DS for both, and look for common node from reversed smaller DS
"""

from collections import OrderedDict


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        pAncestors, qAncestors = self.getAncestors(root, p), self.getAncestors(root, q)

        if len(pAncestors) < len(qAncestors):
            a, b = pAncestors, qAncestors
        else:
            a, b = qAncestors, pAncestors

        for node in reversed(a):
            if node in b:
                return node

    def getAncestors(self, root: TreeNode, targetNode: TreeNode):
        ancestors = OrderedDict()
        found = False

        def dfs(node):
            nonlocal found
            if node and not found:
                ancestors[node] = node.val
                if node.val == targetNode.val:
                    found = True
                elif node.val < targetNode.val:
                    dfs(node.left)
                else:
                    dfs(node.right)

        dfs(root)
        return ancestors
