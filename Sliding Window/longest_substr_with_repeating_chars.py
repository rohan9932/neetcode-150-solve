# 3. Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLen = 0, 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.discard(s[l])
                l += 1
            
            hashset.add(s[r])
            maxLen = max(maxLen, (r-l)+1)

        return maxLen


# Test Case 1
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))

# Test Case 2
print(sol.lengthOfLongestSubstring("bbbbb"))

# Test Case 3
print(sol.lengthOfLongestSubstring("pwwkew"))

# Test Case 4
print(sol.lengthOfLongestSubstring(""))