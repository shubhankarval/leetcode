"""
Problem: Valid Palindrome
Difficulty: Easy
URL: https://leetcode.com/problems/valid-palindrome/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s):
                if self.isValidChar(s[i]):
                    break
                i += 1
            while j > 0:
                if self.isValidChar(s[j]):
                    break
                j -= 1
            if i > len(s) - 1 or j < 0:
                break

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

    def isValidChar(self, char: str) -> bool:
        asc = ord(char)
        if (
            ord("A") <= asc <= ord("Z")
            or ord("a") <= asc <= ord("z")
            or ord("0") <= asc <= ord("9")
        ):
            return True
        return False
