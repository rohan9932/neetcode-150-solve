# 190. Reverse Bits: https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # initialize a fresh var

        for i in range(32):
            lsbbit = n & 1 # pick lsb
            res <<= 1 # make space in res for placing our lsb
            res |= lsbbit # place our lsb x | 0 == x
            n >>= 1 # right shift our n to pick other lsbs

        return res

# Test Case 1
sol = Solution()
print(sol.reverseBits(43261596))  # 964176192

# Test Case 2
print(sol.reverseBits(1))  # 2147483648

# Test Case 3
print(sol.reverseBits(4294967295))  # 4294967295
