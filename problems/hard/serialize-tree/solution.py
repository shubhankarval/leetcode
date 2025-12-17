"""
Problem: Serialize and Deserialize Binary Tree
Difficulty: Hard
URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(w) where w is the maximum width of the tree
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = Queue()
        q.put(root)
        res = ""

        while not q.empty():
            node = q.get()
            if not node:
                res += "_#"
            else:
                res += str(node.val) + "#"
                q.put(node.left)
                q.put(node.right)

        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "_":
            return None

        i, q, root = 0, Queue(), TreeNode()

        root.val, i = self.getVal(data, i)
        q.put(root)

        while i < len(data):
            node = q.get()

            if data[i] != "_":
                node.left = TreeNode()
                node.left.val, i = self.getVal(data, i)
                q.put(node.left)
            else:
                i += 2

            if data[i] != "_":
                node.right = TreeNode()
                node.right.val, i = self.getVal(data, i)
                q.put(node.right)
            else:
                i += 2

        return root

    def getVal(self, data, i):
        val = ""

        while data[i] != "#":
            val += data[i]
            i += 1

        return int(val), i + 1
