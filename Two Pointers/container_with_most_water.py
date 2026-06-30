from typing import List

# 11. Container With Most Water: https://leetcode.com/problems/container-with-most-water/

class Solution:
    # Approach: Two Pointers
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    # The idea is to use two pointers, one at the beginning and one at the end of the array. 
    # We calculate the area formed by the lines at these two pointers and update the maximum area found so far. 
    # Then, we move the pointer pointing to the shorter line inward, as moving the taller line won't help in finding a larger area.
    
    def maxArea(self, height: List[int]) -> int:
        left_bar, right_bar, max_area = 0, len(height)-1, 0

        while left_bar < right_bar:
            # figure out height, width and area
            h = min(height[left_bar], height[right_bar])
            w = right_bar - left_bar
            area = h * w

            # update area if needed
            if area > max_area:
                max_area = area
            
            # update the bars
            if height[left_bar] == h:
                left_bar += 1
            else:
                right_bar -= 1
        
        return max_area

# test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height1))  # Expected output: 49

    # Test case 2
    height2 = [1, 1]
    print(solution.maxArea(height2))  # Expected output: 1

    # Test case 3
    height3 = [4, 3, 2, 1, 4]
    print(solution.maxArea(height3))  # Expected output: 16

    # Test case 4
    height4 = [1, 2, 1]
    print(solution.maxArea(height4))  # Expected output: 2
