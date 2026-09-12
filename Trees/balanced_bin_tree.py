# 110. Balance Binary Tree: https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if root == None:
            return [0, True]
        
        l_info = self.helper(root.left)
        r_info = self.helper(root.right)

        currH = max(l_info[0] , r_info[0]) + 1

        if abs(l_info[0] - r_info[0]) <= 1:
            return [currH, l_info[1] and r_info[1]]
        else:
            return [currH, False]

            
    def isBalanced(self, root):
        return self.helper(root)[1]


# Test Case
solution = Solution()

# Balanced binary tree:
#         3
#        / \
#       9  20
#         /  \
#        15  7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(f"Is Balanced: {solution.isBalanced(root)}")  # Expected: True