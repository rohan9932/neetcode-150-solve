from typing import List

# 1. Two Sum: https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach: Hash Map
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        
        # complement = target - num. Check if complement exists while iterating.
        
        map = {}
        for i in range(len(nums)):
            if (target - nums[i]) in map:
                return [i, map[target-nums[i]]]
            else:
                map[nums[i]] = i
                


if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1 Results: {solution.twoSum(nums1, target1)}")  # Expected Output: [1, 0]

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2 Results: {solution.twoSum(nums2, target2)}")  # Expected Output: [2, 1]

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3 Results: {solution.twoSum(nums3, target3)}")  # Expected Output: [1, 0]