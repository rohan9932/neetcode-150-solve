# 104. Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0

        lDepth = self.maxDepth(root.left)
        rDepth = self.maxDepth(root.right)

        currDepth = 1 + max(lDepth, rDepth)

        return currDepth

# Test Case
solution = Solution()

# Build a binary tree:
#        3
#       / \
#      9  20
#         /  \
#       15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(f"Maximum Depth: {solution.maxDepth(root)}")  # Expected: 3
