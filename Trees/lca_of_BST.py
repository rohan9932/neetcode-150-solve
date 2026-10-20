# 235. Lowest Common Ancestor of a Binary Search Tree: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return

        # left
        if root.left and p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # right
        elif root.right and p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root


# Testcase
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = root.left.right # 4
q = root.left.left # 2
print(Solution().lowestCommonAncestor(root, p, q).val) # Expected: 2
