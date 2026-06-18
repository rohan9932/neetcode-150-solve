# 7. Valid Palindrome: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1: Two Pointers
        # Time Complexity: O(n)
        # Space Complexity: O(n) (for the new string)
        
        # Create a new string that contains only alphanumeric characters in lowercase. Use two pointers to compare characters from the start and end of the new string. If characters are not equal, return False. If pointers meet or cross, return True.
        
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        
        i, j = 0, len(string)-1

        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True
    
    
    def isPalindromeSpaceOptimized(self, s: str) -> bool:
        # Approach 2: Two Pointers (Space Optimized)
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        # Two pointers from ends: skip non-alphanumeric, compare case-insensitive, move inward. One-liner: 'Left and right walk toward center, compare, skip garbage.
        
        i, j = 0, len(s)-1

        while i < j:
            # ignore garbage values
            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Test 1 Results: {solution.isPalindrome(s1)}")  # Expected Output: True
    print(f"Test 1 Space Optimized Results: {solution.isPalindromeSpaceOptimized(s1)}")  # Expected Output: True
    
    # Test Case 2
    s2 = "race a car"
    print(f"Test 2 Results: {solution.isPalindrome(s2)}")  # Expected Output: False
    print(f"Test 2 Space Optimized Results: {solution.isPalindromeSpaceOptimized(s2)}")  # Expected Output: False
