# 8. Valid Parentheses: https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # Approach: Stack
        # Time Complexity: O(n)
        # Space Complexity: O(n) (in worst case, all characters are opening brackets)
        
        # Use a stack to keep track of opening brackets. If we encounter a closing bracket, check if it matches the top element in the stack. If it does, pop from the stack; otherwise, return False. At the end, if the stack is empty, return True; otherwise, return False.
        
        stack = []
        for br in s:
            if br == '(' or br == '{' or br == '[':
                stack.append(br)
            else:
                if len(stack) == 0: # if no opening bracket exists
                    return False
                
                if (br == ')' and stack[-1] == '(') or (br == '}' and stack[-1] == '{') or (br == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False # no match
        
        return len(stack) == 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    s1 = "()"
    print(f"Test 1 Results: {solution.isValid(s1)}")  # Expected Output: True

    # Test Case 2
    s2 = "()[]{}"
    print(f"Test 2 Results: {solution.isValid(s2)}")  # Expected Output: True

    # Test Case 3
    s3 = "(]"
    print(f"Test 3 Results: {solution.isValid(s3)}")  # Expected Output: False

    # Test Case 4
    s4 = "([)]"
    print(f"Test 4 Results: {solution.isValid(s4)}")  # Expected Output: False

    # Test Case 5
    s5 = "{[]}"
    print(f"Test 5 Results: {solution.isValid(s5)}")  # Expected Output: True