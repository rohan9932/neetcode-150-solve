# 7. Reverse Integer: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        rev = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31 - 1)

        x = abs(x)

        while x:
            dig = x % 10
            x = x // 10
            rev = (rev * 10) + dig
        
        if rev > INT_MAX or rev < INT_MIN:
            rev = 0
        elif neg:
            rev = -rev

        return rev

# Test Case 
solution = Solution()
print(f"Test Results: {solution.reverse(123)}")  # Expected Output: 321
print(f"Test Results: {solution.reverse(-123)}")  # Expected Output: -321
print(f"Test Results: {solution.reverse(120)}")  # Expected Output: 21
print(f"Test Results: {solution.reverse(0)}")  # Expected Output: 0
