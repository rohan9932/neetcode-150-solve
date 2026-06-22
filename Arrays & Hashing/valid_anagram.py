# 242. Valid Anagram: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    # Approach 1: Hash Map
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    # Create two hash maps for both strings. Iterate through both strings and populate hash maps with character counts. Compare hash maps for equality.
    
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for ch in s:
            map[ch] = map[ch] + 1 if ch in map else 1
        
        map2 = {}
        for ch in t:
            map2[ch] = map2[ch] + 1 if ch in map2 else 1
        
        return map == map2
    
# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Test 1 Results: {solution.isAnagram(s1, t1)}")  # Expected Output: True

    # Test Case 2
    s2 = "rat"
    t2 = "car"
    print(f"Test 2 Results: {solution.isAnagram(s2, t2)}")  # Expected Output: False