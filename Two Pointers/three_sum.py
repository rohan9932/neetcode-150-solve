from typing import List

# 15. 3Sum: https://leetcode.com/problems/3sum/

class Solution:
    # Approach: Two Pointers
    # Time Complexity: O(n^2)
    # Space Complexity: O(n) for storing the result in a set

    # first for each num set target by 0 - nums[i] then use two pointers to find the target sum in the rest of the array
    # store the result in a set to avoid duplicates and finally return the result as a list of lists

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # for applying 2 pointers in inner loop
        temp = set()

        for i in range(len(nums)-2): # so that not idx bound of array for j and k
            target = 0 - nums[i] # as nums[i] + target == 0
            # two sum logic
            j, k = i+1, len(nums)-1

            while j < k:
                summation = nums[j] + nums[k]
                if summation == target:
                    temp.add((nums[i], nums[j], nums[k]))
                    # for checking next elements
                    j += 1
                    k -= 1
                elif summation < target:
                    j += 1
                else:
                    k -= 1

        return [list(x) for x in temp]


# test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums1))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]

    # Test case 2
    nums2 = [0, 0, 0]
    print(solution.threeSum(nums2))  # Expected output: [[0, 0, 0]]

    # Test case 3
    nums3 = [3, -2, 1, 0]
    print(solution.threeSum(nums3))  # Expected output: []

    # Test case 4
    nums4 = [-2, 0, 1, 1, 2]
    print(solution.threeSum(nums4))  # Expected output: [[-2, 0, 2], [-2, 1, 1]]
