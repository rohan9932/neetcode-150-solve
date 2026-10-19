# 199. Binary Tree Right Side View: https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root == None:
            return []
            
        queue = deque([root])
        ans = []

        while len(queue) > 0:
            lvlLen = len(queue)
            for i in range(lvlLen):
                front = queue.popleft()
                if i == lvlLen-1:
                    ans.append(front.val)
                
                if front.left:
                    queue.append(front.left)
                
                if front.right:
                    queue.append(front.right)
        
        return ans

# Test Case
solution = Solution()

# Tree with right side view: [1, 3, 4]
#         1
#        / \
#       2   3
#      / \
#     4   5
# Expected: [1, 3, 5]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"Right side view: {solution.rightSideView(root)}")


# Test Case 2:
# Tree: []
# Expected: []

print(f"Right side view: {solution.rightSideView(None)}")

# Test Case 3:

# Tree:
#         1
#        / 
#       2  
# Expected: [1, 2]

root = TreeNode(1)
root.left = TreeNode(2)
print(f"Right side view: {solution.rightSideView(root)}")

