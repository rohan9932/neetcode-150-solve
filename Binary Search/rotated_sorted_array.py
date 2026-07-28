from typing import List

# 33. Search in Rotated Sorted Array: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums)-1

        while st <= end:
            mid = (st + end)//2

            if nums[mid] == target:
                return mid

            # case 01 -> mid in left sorted
            if nums[st] <= nums[mid]:
                if target > nums[mid] or target < nums[st]:
                    st = mid + 1
                else:
                    end = mid - 1
            # case 02 -> mid in right sorted
            else:
                if target < nums[mid] or target > nums[end]:
                    end = mid - 1
                else:
                    st = mid + 1
        
        return -1
    

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(f"Test 1 Results: {solution.search(nums1, target1)}")  # Expected Output: 4

    # Test Case 2
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(f"Test 2 Results: {solution.search(nums2, target2)}")  # Expected Output: -1

    # Test Case 3
    nums3 = [1]
    target3 = 0
    print(f"Test 3 Results: {solution.search(nums3, target3)}")  # Expected Output: -1