# 226. Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root):
        if root == None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        # call in depth
        self.invertTree(root.left) 
        self.invertTree(root.right)

        return root


# Test Case
solution = Solution()

# Creating a binary tree for testing
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Use preorder to make the tree structure easy to read
# Root -> Left -> Right

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

print("Original Tree (Inorder):")
print_inorder(root)  # Expected: 1 2 3 4 6 7 9
print("\n")

inverted_root = solution.invertTree(root)
print("Inverted Tree (Inorder):")
print_inorder(inverted_root)  # Expected: 9 7 6 4 3 2 1
print()
