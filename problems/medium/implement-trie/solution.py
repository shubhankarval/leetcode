"""
Problem: Implement Trie (Prefix Tree)
Difficulty: Medium
URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Time Complexity: O(m) where m is the length of the word
Space Complexity: O(N * M) where N is the number of words and M is the average word length
"""


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node, i = self.root, 0
        while i < len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i += 1
        while i < len(word):
            node.children[word[i]] = node = TrieNode(word[i])
            i += 1
        node.isWord = True

    def search(self, word: str) -> bool:
        return self.findString(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self.findString(prefix, False)

    def findString(self, s: str, isWord: bool) -> bool:
        node = self.root
        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False
        return node.isWord if isWord else True


class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.isWord = False
        self.children = {}  # val -> node
