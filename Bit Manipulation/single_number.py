from typing import List

# 136. Single Number: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]

        for i in range(1, len(nums)):
            ans ^= nums[i]
        
        return ans

# Test Case 1
sol = Solution()
print(sol.singleNumber([2, 2, 1]))

# Test Case 2
print(sol.singleNumber([4, 1, 2, 1, 2]))

# Test Case 3
print(sol.singleNumber([1]))
