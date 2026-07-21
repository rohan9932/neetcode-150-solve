from typing import List
import math

# 875. Koko Eating Bananas: https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxVal= 0

        for i in range(len(piles)):
            maxVal = max(maxVal, piles[i])
        
        k = maxVal

        low, high = 1, maxVal # searching in the answer k range

        while low <= high:
            k_prime = (low+high)//2

            # getting total hour at this speed
            hrs = 0
            for i in range(len(piles)):
                hrs += math.ceil(piles[i]/k_prime)

            # need to eat more banana per hour to finish
            if hrs > h:
                low = k_prime + 1
            # could be possible k. need to check on lesser values further
            else:
                k = k_prime
                high = k_prime - 1

        return k

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    piles = [3,6,7,11]
    h = 8
    print(solution.minEatingSpeed(piles, h))  # Expected Output: 4
    # Test Case 2
    piles = [30,11,23,4,20]
    h = 5
    print(solution.minEatingSpeed(piles, h))  # Expected Output: 30
