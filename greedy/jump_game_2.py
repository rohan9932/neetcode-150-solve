# 45. Jump Game II: https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jumpGreedy(self, nums: list[int]) -> int:
        res = 0
        l, r = 0, 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            
            l = r+1
            r = farthest
            res += 1
        
        return res

    def jump(self, nums: list[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            j = nums[i]
            mini = dp[i+1]
            for k in range(2, j+1):
                if i + k < len(nums):
                    mini = min(mini, dp[i+k])
            
            dp[i] = mini + 1
        
        return dp[0]

# Test Case 
solution = Solution()
print(f"Test Results: {solution.jumpGreedy([2,3,1,1,4])}") # Expected Output: 2
print(f"Test Results: {solution.jumpGreedy([2,3,0,1,4])}") # Expected Output: 2

print(f"Test Results: {solution.jump([2,3,1,1,4])}") # Expected Output: 2
print(f"Test Results: {solution.jump([2,3,0,1,4])}") # Expected Output: 2
