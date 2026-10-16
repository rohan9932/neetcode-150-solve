from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []

        queue = deque([root])

        ans = []

        while queue:
            lvlLen = len(queue)
            lvlNodes = []

            for _ in range(lvlLen):
                front = queue.popleft()
                lvlNodes.append(front.val)

                if front.left:
                    queue.append(front.left)
                
                if front.right:
                    queue.append(front.right)
            
            ans.append(lvlNodes)
        
        return ans



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.levelOrder(root))

