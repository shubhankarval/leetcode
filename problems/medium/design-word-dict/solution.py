"""
Problem: Design Add and Search Word Data Structure
Difficulty: Medium
URL: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Time Complexity:
addWord(): O(m) where m is the word length
search(): O(26^2 * m) = O(m) where m is the word length

Space Complexity: O(N * M) where N is the number of words and M is the average word length
"""


class TrieNode:
    def __init__(self):
        self.children = {}  # val -> node
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False
            if i == len(word):
                return node.isWord
            if word[i] == ".":
                for n in node.children.values():
                    if dfs(n, i + 1):
                        return True
            if word[i] in node.children:
                return dfs(node.children[word[i]], i + 1)
            return False

        return dfs(self.root, 0)
