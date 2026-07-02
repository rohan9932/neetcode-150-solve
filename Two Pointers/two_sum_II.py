from typing import List

# 167. Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    # Approach: Two pointers
    # Time complexity: O(n) - iterate through the array once
    # Space complexity: O(1) - use two pointers
    
    # if the sum of the two numbers is less than target then increment i
    # if the sum is greater than target then decrement j
    # if sum found return [i+1, j+1] because it's one based index
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], 9)) # [1,2]
    print(s.twoSum([2,3,4], 6)) # [1,3]
