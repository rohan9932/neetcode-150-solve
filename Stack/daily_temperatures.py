from typing import List

# 739. Daily Temperatures: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # here we can use monotonic decreasing stack approach
        # here we need next greater temp and the day diff with it
        # 1. we use monotonic decreasing stack
        # 2. store the idx in stack
        # 3. store s.top().idx - curr idx and store in ans
        # 4. if s.empty() store 0 (no greater temp in this case)

        stack = []
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            # to store only the next greater elements
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) != 0: # as arr initialized with 0 so no greater element case already handled
                ans[i] = stack[-1] - i # day diff
            
            stack.append(i)
        
        return ans
    
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]
    print(s.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70])) # [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
    