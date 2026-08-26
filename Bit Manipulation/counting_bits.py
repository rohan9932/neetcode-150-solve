from typing import List

# 338. Counting Bits: https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1): # check for 0 to n
            # figure out hamming weight of the i
            no_bits = 0
            temp = i
            while temp:
                if temp & 1 == 1: # num will be 1 eg. 101 & 001 == 1 if LSB == 1
                    no_bits += 1
                
                temp >>= 1 # right shift to go through every bit
            
            # append to ans array
            ans.append(no_bits)
        
        return ans

# Test Case 1
sol = Solution()
print(sol.countBits(5))  # 0->0, 1->1, 2->1, 3->2, 4->1, 5->2

# Test Case 2
print(sol.countBits(0))  # 0->0

# Test Case 3
print(sol.countBits(2))  # 0->0, 1->1, 2->1
