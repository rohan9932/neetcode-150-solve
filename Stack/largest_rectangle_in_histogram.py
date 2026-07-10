from typing import List

# 84. Largest Rectangle in Histogram: https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    # Approach: Monotonic Stack in both

    # Time Complexity: O(3n) -> O(n) 
    # Space Complexity: O(3n) -> O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        prev_smaller, next_smaller = [-1] * len(heights), [len(heights)] * len(heights)
        # prev smaller -1 initialization handles the edge case when there is only one bar

        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]: 
                stack.pop() # as we want the pse in top
            
            if len(stack) != 0:
                prev_smaller[i] = stack[-1]
            
            stack.append(i)
            
        stack = []

        for i in range(len(heights)-1, -1, -1):
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                stack.pop() # as we want nse in top
            
            if len(stack) != 0:
                next_smaller[i] = stack[-1]

            stack.append(i)

        maxArea = 0
        
        # for each bar we figure out max rectangle area it can make
        # as any bar can't go through if there is a smaller bar before or after
        # so we just find previous smaller bar and next smaller bar
        # and the gap between them is the max width possible for each bar
        for i in range(len(heights)):
            area = heights[i] * (next_smaller[i] - prev_smaller[i] - 1)
            maxArea = max(area, maxArea)
        
        return maxArea

    # Time Complexity: O(n)
    # Space Complexity: O(2n) -> O(n)
    def largestRectangleAreaOptimalOnePass(self, heights: List[int]) -> int:
        # our intuition is we need area for each bar and update maxArea
        # so our height would be h[i] for ith bar
        # and width is basically (nse-pse)-1
        # because we can see our bar can't go pass through bars which are smaller than it

        stack = []
        prev_smaller = [-1] * len(heights) # as nse will count while popping an element

        maxArea = 0

        for i in range(len(heights)):
            # popping which are not pse to this element
            while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                # before popping we need to calculate for the bar we are going to pop
                # because technically we have pse as we traversed forward
                # and now as we are popping a back element we have the nse also
                # because for this element as our s.top() element is bigger than it
                # so the element is just nse for our top

                area = heights[stack[-1]] * (i - prev_smaller[stack[-1]] - 1)
                maxArea = max(area, maxArea)

                stack.pop()
            
            # now we just calculate regular pse
            if len(stack) != 0:
                prev_smaller[i] = stack[-1]
            
            stack.append(i)

        # for rest elements in stack they have no nse
        # so we need to pick nse as the len(heights) and calculate area for them
        while len(stack) != 0:
            area = heights[stack[-1]] * (len(heights) - prev_smaller[stack[-1]] - 1)
            maxArea = max(area, maxArea)
            stack.pop()

        return maxArea


# Test Cases
if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleAreaOptimalOnePass([2,1,5,6,2,3])) # 10
    print(s.largestRectangleArea([2, 4])) # 4
