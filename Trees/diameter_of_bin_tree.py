# 543. Diameterr of Binary Tree: https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if root == None:
            return [0, 0]
        
        l_info = self.helper(root.left)
        r_info = self.helper(root.right)

        currH = max(l_info[0], r_info[0]) + 1
        
        op1 = l_info[1]
        op2 = r_info[1]
        op3 = l_info[0] + r_info[0]

        return [currH, max(op1, max(op2, op3))]

    def diameterOfBinaryTree(self, root):
        return self.helper(root)[1]


# Test Case
solution = Solution()

# Tree with diameter 3:
#         1
#        / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"Diameter: {solution.diameterOfBinaryTree(root)}")  # Expected: 3
