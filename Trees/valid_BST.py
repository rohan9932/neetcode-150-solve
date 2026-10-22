# 98. Validate Binary Search Tree: https://leetcode.com/problems/validate-binary-search-tree/

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root: TreeNode | None, inorderList: List[int]) -> None:
        if root == None:
            return 
        
        self.inorder(root.left, inorderList)
        inorderList.append(root.val)
        self.inorder(root.right, inorderList)

    def isValidBST(self, root: TreeNode | None) -> bool:
        inorderList = []
        self.inorder(root, inorderList)

        isBst = True

        for i in range(1, len(inorderList)):
            if inorderList[i] <= inorderList[i-1]:
                isBst = False
                break
        
        return isBst


# Test cases
sol = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)
print(sol.isValidBST(root)) # Expected: False

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(sol.isValidBST(root)) # Expected: True
