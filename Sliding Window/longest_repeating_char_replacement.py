from collections import defaultdict

# 424. Longest Repeating Character Replacement: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxLen = 0, 0
        map = defaultdict(int)

        for r in range(len(s)):
            map[s[r]] += 1
            
            # not violates
            if (r-l+1)-max(map.values(), default=0) <= k:
                maxLen = max(maxLen, (r-l+1))
            else:
                map[s[l]] -= 1
                l += 1

        return maxLen


# Test Case 1
sol = Solution()
print(sol.characterReplacement("ABAB", 2))

# Test Case 2
print(sol.characterReplacement("AABABBA", 1))

# Test Case 3
print(sol.characterReplacement("AAAAA", 2))

# Test Case 4
print(sol.characterReplacement("ABBB", 2))