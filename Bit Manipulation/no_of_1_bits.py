# 191. No. of 1 bits: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            if (n & 1) == 1: # eg. 101 & 001 == 001(1) so the lsb is 1
                ans += 1
            
            n >>= 1 # right shift
        
        return ans


# Test Case 1
sol = Solution()
print(sol.hammingWeight(11))  # 1011 -> 3

# Test Case 2
print(sol.hammingWeight(128))  # 10000000 -> 1

# Test Case 3
print(sol.hammingWeight(0))  # 0 -> 0
