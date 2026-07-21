from typing import List

# 704. Binary Search: https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums)-1
        while st <= end:
            mid = (st+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st = mid+1
            else:
                end = mid-1
        
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    print(f"Test 1 Results: {solution.search(nums1, target1)}")  # Expected Output: 4

    # Test Case 2
    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    print(f"Test 2 Results: {solution.search(nums2, target2)}")  # Expected Output: -1

    # Test Case 3
    nums3 = [5]
    target3 = 5
    print(f"Test 3 Results: {solution.search(nums3, target3)}")  # Expected Output: 0