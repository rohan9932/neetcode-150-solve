# 55. Jump Game: https://leetcode.com/problems/jump-game/

class Solution:
    # the idea is to go backwards and check if we can come to goal from that idx
    # if we can we move the goal forward to that idx
    # and in the end we check if the goal has come to the first idx
    
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

# Test Case
sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
