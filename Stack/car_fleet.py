from typing import List

# 853. Car Fleet: https://leetcode.com/problems/car-fleet/

class Solution:
    # Time Complexity: O(nlogn) - sorting the cars based on position
    # Space Complexity: O(n) - for the stack and new_arr
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        new_arr = []
        for i in range(len(position)):
            new_arr.append((position[i], speed[i]))
        
        new_arr.sort() # sorting the cars based on position as relative position will not be tampered

        for i in range(len(new_arr)-1, -1, -1):
            if len(stack) == 0: # pushing last car to stack
                t = (target-new_arr[i][0]) / new_arr[i][1]
                stack.append(t)
            else: # comparing curr car with next car's time. if takes less time then surely will be a fleet with the next car
                t1 = (target-new_arr[i][0]) / new_arr[i][1]
                t2 = stack[-1]

                if t1 > t2:
                    stack.append(t1)
        
        return len(stack)


# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])) # 3
    print(s.carFleet(10, [3], [3])) # 1
    print(s.carFleet(100, [0, 2, 4], [4, 2, 1])) # 1

