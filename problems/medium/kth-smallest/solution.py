"""
Problem: Kth Smallest Integer in BST
Difficulty: Medium
URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

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
travese in left-first manner
decrement k
early termination 
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal k, ans
            if not node or k == 0:
                return

            dfs(node.left)

            if k > 0:
                k -= 1
                if k == 0:
                    ans = node.val
                    return

            dfs(node.right)

        dfs(root)
        return ans
