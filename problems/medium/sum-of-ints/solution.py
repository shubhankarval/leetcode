"""
Problem: Sum of Two Integers
Difficulty: Medium
URL: https://leetcode.com/problems/sum-of-two-integers/

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a >= 0 and b >= 0:
            return self.add(a, b)
        if a < 0 and b < 0:
            return -self.add(abs(a), abs(b))

        m, n = max(abs(a), abs(b)), min(abs(a), abs(b))
        diff = self.subtract(m, n)
        if (m == abs(a) and a > 0) or (m == abs(b) and b > 0):
            return diff
        return -diff 

    def add(self, a: int, b: int) -> int:
        res = rem = shift = 0

        while a or b or rem:
            bit1, bit2 = a & 1, b & 1
            s = rem + bit1 + bit2
            if s % 2:
                res |= 1 << shift

            rem = 1 if s >= 2 else 0
            shift += 1
            a >>= 1
            b >>= 1

        return res
    
    def subtract(self, a: int, b: int) -> int:
        res = borrow = shift = 0
        while a:
            bit1, bit2 = a & 1, b & 1
            if borrow:
                if bit1:
                    bit1 = borrow = 0
                else:
                    bit1 = 1
                    
            diff = bit1 - bit2
            if diff != -1:
                res += (diff << shift)
            else:
                res += 1 << shift
                borrow = 1
            
            shift += 1
            a >>= 1
            b >>= 1
        return res
