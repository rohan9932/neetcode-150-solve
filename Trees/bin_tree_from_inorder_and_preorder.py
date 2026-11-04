# 105. Construct binary tree from inorder and preorder: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, inorderMap, preorder, inorder, inSt, inEnd, preSt):
        if preSt >= len(preorder) or (inSt > inEnd):
            return
        
        root = TreeNode(preorder[preSt])
        inorderIdx = inorderMap[preorder[preSt]]

        lPreSt = preSt + 1
        rPreSt = preSt + inorderIdx-inSt + 1

        root.left = self.helper(inorderMap, preorder, inorder, inSt, inorderIdx-1, lPreSt)
        root.right = self.helper(inorderMap, preorder, inorder, inorderIdx+1, inEnd, rPreSt)

        return root

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        m = {}

        for i in range(len(inorder)):
            m[inorder[i]] = i
        
        return self.helper(m, preorder, inorder, 0, len(inorder)-1, 0)


def print_tree(node): # preorder traversal
    if not node:
        return
    print(node.val, end=" ")
    print_tree(node.left)
    print_tree(node.right)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

sol = Solution()
root = sol.buildTree(preorder, inorder)

print("Constructed Tree (Pre-order verification):")
print_tree(root)
print()