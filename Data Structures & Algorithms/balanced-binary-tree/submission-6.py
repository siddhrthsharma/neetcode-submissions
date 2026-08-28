# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> int:
        self.difference = 1
        
        def dfs(node):
            if not node:
                return 0
        
            l = dfs(node.left)
            r = dfs(node.right)

            self.difference = max(self.difference, abs(l-r))

            return 1 + max(l, r)
       
        dfs(root)
        return self.difference <= 1

            
            

        