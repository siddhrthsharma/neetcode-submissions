# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(root):
            if not root:
                return None
            
            l = dfs(root.left)
            res.append(root.val)
            r = dfs(root.right)

        dfs(root)
        return all(res[i] < res[i+1] for i in range(len(res) - 1))

