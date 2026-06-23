from typing import List
import heapq

# 347. Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/description/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach: Min Heap
        # Time Complexity: O(n log k)
        # Space Complexity: O(n)
        
        # Create a hash map to store the frequency of each number in nums.
        # Create a min heap to store the k most frequent elements. (frequency, number) pair
        # Iterate through the hash map and push elements into the heap. If the size of the heap 
        # exceeds k, pop the smallest element from the heap.
        # Return the elements in the heap.

        map = {}

        for num in nums:
            map[num] = 1 if not num in map else map[num] + 1 # frequency count
        
        min_heap = []
        k_counter = k
        
        for key, value in map.items():
            if k_counter > 0:
                heapq.heappush(min_heap, (value, key)) # pushing as (freq, num)
                k_counter -= 1
            else:
                if value > min_heap[0][0]: # peeking top element
                    # heapq.heappop(min_heap)
                    # heapq.heappush(min_heap, (value, key))
                    heapq.heappushpop(min_heap, (value, key))
        
        ans = []
        while min_heap:
            smallest = heapq.heappop(min_heap)
            ans.append(smallest[1])
        
        return ans


# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(f"Test 1 Results: {solution.topKFrequent(nums1, k1)}")  # Expected Output: [1, 2]

    # Test Case 2
    nums2 = [1]
    k2 = 1
    print(f"Test 2 Results: {solution.topKFrequent(nums2, k2)}")  # Expected Output: [1]