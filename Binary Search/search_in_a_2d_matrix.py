from typing import List

# 74. Search a 2D Matrix: https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    # Time Complexity: O(log(m*n))
    # Space Complexity: O(1)

    # We treated matrix as a single sorted array, and performed binary search on it.
    # row_idx = mid_cell // col_len
    # col_idx = mid_cell % col_len

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])

        st_cell, end_cell = 0, (row_len*col_len)-1

        while st_cell <= end_cell:
            mid_cell = (st_cell+end_cell)//2
            row_idx = mid_cell // col_len
            col_idx = mid_cell % col_len
            mid_num = matrix[row_idx][col_idx]

            if mid_num == target:
                return True
            elif mid_num > target:
                end_cell = mid_cell - 1
            else:
                st_cell = mid_cell + 1

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    print(solution.searchMatrix(matrix, target))  # Expected Output: True
    # Test Case 2
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(solution.searchMatrix(matrix, target))  # Expected Output: False
