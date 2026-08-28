from typing import List

# 268. Missing Number: https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sum of n natural numbers is (n(n+1))/2
        # If we find the difference between the expected sum and the actual sum, we get the missing number
        n = len(nums)
        exp_sum = (n*(n+1))//2
        act_sum = sum(nums)
        return exp_sum - act_sum

    def missingNumberXOR(self, nums: List[int]) -> int:
        # a XOR a == 0. So if we xor all the numbers with their corresponding indices, the result will be the missing number
        ans = 0

        for i in range(len(nums)):
            ans ^= i ^ nums[i]

        # xor with n as well
        ans ^= len(nums)

        return ans


# Test Case 1
sol = Solution()
print(sol.missingNumber([3, 0, 1]))
print(sol.missingNumberXOR([3, 0, 1]))

# Test Case 2
print(sol.missingNumber([0, 1]))
print(sol.missingNumberXOR([0, 1]))

# Test Case 3
print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(sol.missingNumberXOR([9, 6, 4, 2, 3, 5, 7, 0, 1]))
