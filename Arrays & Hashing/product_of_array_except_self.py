from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        # Initialize two arrays to store the product of elements on the left and right sides of each element.
        # Initialize the product of elements on the left and right sides to 1.
        # Iterate through the array from left to right, updating the product of elements on the left side.
        
        left_prod = [1 for num in nums]
        right_prod = [1 for num in nums]

        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            nums[i] = left_prod[i] * right_prod[i]

        return nums 
    
# Test cases
if  __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4])) # [24,12,8,6]
    print(solution.productExceptSelf([-1,1,0,-3,-9])) # [0, 0, -27, 0, 0]
    print(solution.productExceptSelf([0,0])) # [0,0]
