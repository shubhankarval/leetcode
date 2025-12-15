"""
Problem: Subtree of Another Tree
Difficulty: Easy
URL: https://leetcode.com/problems/subtree-of-another-tree/

Time Complexity: O(n * m) - n is number of nodes in root, m is number of nodes in subRoot
Space Complexity: O(h1 + h2) - h1 is height of root, h2 is height of subRoot
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Intuition:
If root val == subRoot val, see if same tree
if yes the retrun true
else continue traversing left and right
"""


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
                root.right, subRoot.right
            )

        return False
