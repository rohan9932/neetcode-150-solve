from typing import List

# 2. Contains Duplicate: https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    # Approach 1: Set
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    # Convert array to set and compare lengths. If set length is less than array length, there are duplicates.
    
    def containsDuplicate1(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
    
    # Approach 2: Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    # Hash set 0(1) for uniquness check. Iterate through array and check if element is in set. If it is, return True. Else, add element to set.
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            else:
                map[nums[i]] = i
        
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1 Results: {solution.containsDuplicate1(nums1)}")  # Expected Output: False
    print(f"Test 1 Results: {solution.containsDuplicate2(nums1)}")  # Expected Output: False

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Test 2 Results: {solution.containsDuplicate1(nums2)}")  # Expected Output: False
    print(f"Test 2 Results: {solution.containsDuplicate2(nums2)}")  # Expected Output: False

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Test 3 Results: {solution.containsDuplicate1(nums3)}")  # Expected Output: True
    print(f"Test 3 Results: {solution.containsDuplicate2(nums3)}")  # Expected Output: True