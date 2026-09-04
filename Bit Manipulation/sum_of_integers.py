# 371. Sum of Integers: https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 1. Handle Python's arbitrary-precision integers by simulating 32-bit behavior.
        # MASK handles the lower 32 bits.
        # MAX_INT is used to detect overflow and convert back from two's complement representation.
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # carry now contains common set bits of a and b (and shifted left)
            carry = ((a & b) << 1) & MASK
            # sum of bits of a and b where at least one of the bits is not set
            a = (a ^ b) & MASK
            b = carry

        return a if a <= MAX_INT else ~(a ^ MASK)


# Test Case 1
sol = Solution()
print(sol.getSum(1, 2))

# Test Case 2
print(sol.getSum(2, 3))

# Test Case 3
print(sol.getSum(-1, 1))
