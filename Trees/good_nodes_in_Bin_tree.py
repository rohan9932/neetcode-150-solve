# 1448. Count Good Nodes in Binary Tree: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, currPathMax):
        if root == None:
            return 0

        goodNodes = 0
        newCurrPathMax = currPathMax

        if root.val >= currPathMax:
            newCurrPathMax = root.val
            goodNodes += 1
        
        left = self.inorder(root.left, newCurrPathMax)
        right = self.inorder(root.right, newCurrPathMax)

        goodNodes += left + right

        return goodNodes

    def goodNodes(self, root: TreeNode) -> int:
        return self.inorder(root, root.val)


# Test cases
sol = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(4)
print(sol.goodNodes(root)) # Expected: 4
