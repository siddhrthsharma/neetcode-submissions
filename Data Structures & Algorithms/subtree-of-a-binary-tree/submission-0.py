# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def sameTree(self, r, s):
        def dfs(r, s):
            if not r and not s:
                return True
            if (r and not s) or (s and not r):
                return False
            if r.val != s.val:
                return False
            
            return dfs(r.left, s.left) and dfs(r.right, s.right)

        return dfs(r, s)
            

                        

            