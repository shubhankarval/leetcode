"""
Problem: Group Anagrams
Difficulty: Medium
URL: https://leetcode.com/problems/group-anagrams/

Time Complexity: O(n * m log m) where n is number of strings, m is max length
Space Complexity: O(n * m)
"""

from typing import List
from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Optimal approach using sorted string as key.

        Anagrams will have the same sorted string representation.

        Time Complexity: O(n * m log m) - sorting each string
        Space Complexity: O(n * m) - storing all strings in hash map
        """
        tracker = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            tracker[sorted_s].append(s)
        return list(tracker.values())


def test_solution():
    solution = Solution()

    # Test case 1: Basic anagrams
    result1 = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Convert result to set of frozensets for order-independent comparison
    result1_sets = {frozenset(group) for group in result1}
    expected1_sets = {
        frozenset(["bat"]),
        frozenset(["nat", "tan"]),
        frozenset(["ate", "eat", "tea"]),
    }
    assert (
        result1_sets == expected1_sets
    ), f"Expected {expected1_sets}, got {result1_sets}"
    assert len(result1) == 3, f"Expected 3 groups, got {len(result1)}"

    # Test case 2: Empty string
    result2 = solution.groupAnagrams([""])
    assert len(result2) == 1 and result2[0] == [""], f"Expected [['']], got {result2}"

    # Test case 3: Single character
    result3 = solution.groupAnagrams(["a"])
    assert len(result3) == 1 and result3[0] == ["a"], f"Expected [['a']], got {result3}"

    # Test case 4: No anagrams
    result4 = solution.groupAnagrams(["abc", "def", "ghi"])
    assert len(result4) == 3, f"Expected 3 groups, got {len(result4)}"
    # Each group should have exactly one element
    for group in result4:
        assert len(group) == 1, f"Each group should have 1 element, got {len(group)}"

    # Test case 5: All same strings
    result5 = solution.groupAnagrams(["abc", "abc", "abc"])
    assert len(result5) == 1, f"Expected 1 group, got {len(result5)}"
    assert len(result5[0]) == 3, f"Expected group of 3 elements, got {len(result5[0])}"
    assert all(s == "abc" for s in result5[0]), f"All elements should be 'abc'"

    # Test case 6: Check anagram property
    result6 = solution.groupAnagrams(["listen", "silent", "hello", "world"])
    # Find the group containing "listen"
    listen_group = None
    for group in result6:
        if "listen" in group:
            listen_group = group
            break
    assert listen_group is not None, "listen should be in one of the groups"
    assert "silent" in listen_group, "silent should be in the same group as listen"
    assert len(result6) == 3, f"Expected 3 groups, got {len(result6)}"

    print("All test cases passed!")


if __name__ == "__main__":
    test_solution()
