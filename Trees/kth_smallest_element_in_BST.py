# 230. Kth Smallest Element in a BST: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, inorderlist):
        if root == None:
            return None
        
        self.inorder(root.left, inorderlist)
        inorderlist.append(root.val)
        self.inorder(root.right, inorderlist)

    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        inorderList = []
        self.inorder(root, inorderList)

        return inorderList[k-1]


# Test Case

sol = Solution()

# Tree
#       3
#      / \
#     1   4
#      \
#       2

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

print(sol.kthSmallest(root, 3)) # Expected output: 3
