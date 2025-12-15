"""
Problem: Count Good Nodes in Binary Tree
Difficulty: Medium
URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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
DFS - pass a prevMaxVal param so we can identify a good node
keep a count var, and increment it when good node found
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, prevMax):
            nonlocal count
            if node:
                if node.val >= prevMax:
                    count += 1
                    prevMax = node.val

                dfs(node.left, prevMax)
                dfs(node.right, prevMax)

        dfs(root, float("-inf"))
        return count
