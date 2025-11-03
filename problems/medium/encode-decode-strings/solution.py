"""
Problem: Encode and Decode Strings
Difficulty: Medium
URL: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(list(map(lambda x: str(len(x)) + "_" + x, strs)))

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            length, word_start = int(s[i:j]), j + 1
            word_end = word_start + length
            res.append(s[word_start:word_end])
            i = word_end
        return res
