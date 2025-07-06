"""
Problem: Valid Anagram
Difficulty: Easy
URL: https://leetcode.com/problems/valid-anagram/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_solution():
    solution = Solution()

    # Test case 1: Valid anagram
    result1 = solution.isAnagram("anagram", "nagaram")
    assert result1 == True, f"Expected True, got {result1}"

    # Test case 2: Not an anagram
    result2 = solution.isAnagram("rat", "car")
    assert result2 == False, f"Expected False, got {result2}"

    # Test case 3: Empty strings
    result3 = solution.isAnagram("", "")
    assert result3 == True, f"Expected True, got {result3}"

    # Test case 4: Different lengths
    result4 = solution.isAnagram("abc", "abcd")
    assert result4 == False, f"Expected False, got {result4}"

    # Test case 5: Same string
    result5 = solution.isAnagram("listen", "listen")
    assert result5 == True, f"Expected True, got {result5}"

    # Test case 6: Single character
    result6 = solution.isAnagram("a", "a")
    assert result6 == True, f"Expected True, got {result6}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
