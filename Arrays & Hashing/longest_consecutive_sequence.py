from typing import List

# 128. Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    # Approach: Hash set + iteration through the array to find longest consecutive sequence.
    # Time complexity: O(n) - iterate through the array once
    # Space complexity: O(n) - use hash
    
    # take all nums as a hash set to check for existence of numbers in O(1) time
    # iterate through array and check if it's the beginning of a consecutive sequence. 
    # If not skip
    # If it is then check for the next number in the sequence and keep counting until it's not found.
    # Update the longest consecutive sequence length if needed.
    
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_count = 0

        for num in hash_set:
            if num-1 not in hash_set: # checking if beginning number
                # for every beggining sequence count the consecutive sequence length
                count = 1
                consecutive_next = num + 1
                while consecutive_next in hash_set:
                    count += 1
                    consecutive_next += 1
                
                # update with max_length if needed
                max_count = max(max_count, count)
                
        return max_count # max sequence length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2])) # 4
    print(solution.longestConsecutive([0,1,2,3,4,5])) # 6
