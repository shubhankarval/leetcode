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
Conditions:
p,q both lesser or greather than node then move left or right
p == node, q == node, p,q one is lesser, another is greater then return node
"""


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
