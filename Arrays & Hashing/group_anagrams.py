from typing import List
from collections import defaultdict

# 49. Group Anagrams: https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach: Hash Map
        # Time Complexity: O(n * k log k) 
        # where n is the number of strings and k is the maximum length of a string (due to sorting)
        # Space Complexity: O(n * k) for the hash map storing the groups of anagrams
        
        # Use a hash map to group anagrams together. The key will be the sorted version of the
        # string, and the value will be a list of strings that are anagrams of each other.

        map = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str)) # str sort
            map[sorted_str].append(str) # group anagram values
        
        ans = []

        for key, value in map.items():
            ans.append(map[key]) # store the groups in the answer
        
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # Expected Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    print(solution.groupAnagrams([""]))  # Expected Output: [[""]]
    print(solution.groupAnagrams(["a"]))  # Expected Output: [["a"]]
    print(solution.groupAnagrams(["abc", "bca", "cab", "xyz", "zyx"]))  # Expected Output: [["abc", "bca", "cab"], ["xyz", "zyx"]]
