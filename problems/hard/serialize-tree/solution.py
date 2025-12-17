"""
Problem: Serialize and Deserialize Binary Tree
Difficulty: Hard
URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

serialize() -
Time Complexity: O(n)
Space Complexity: O(w)

deserialize() -
Time Complexity: O(n)
Space Complexity: O(n)

where n is the number of nodes in the tree and w is the maximum width of the tree
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
                res += "-#"
            else:
                res += str(node.val) + "#"
                q.put(node.left)
                q.put(node.right)

        return res[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("#")
        if data[0] == "-":
            return None

        q = Queue()
        root = TreeNode(int(data[0]))
        q.put(root)

        for i in range(1, len(data) - 1, 2):
            node = q.get()

            if data[i] != "-":
                node.left = TreeNode(int(data[i]))
                q.put(node.left)

            if data[i + 1] != "-":
                node.right = TreeNode(int(data[i + 1]))
                q.put(node.right)

        return root
