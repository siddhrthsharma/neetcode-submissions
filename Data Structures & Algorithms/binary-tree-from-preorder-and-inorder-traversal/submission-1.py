# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd:
                return None

            root_val = preorder[preStart]
            root = TreeNode(root_val)
            mid = inorder_map[root_val]

            left_size = mid - inStart

            root.left = build(preStart + 1, preStart + left_size, inStart, mid - 1)
            root.right = build(preStart + left_size + 1, preEnd, mid + 1, inEnd)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
