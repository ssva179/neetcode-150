# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#pseudocode:
#if not root: -> root == null
    #return 
#tmp = root.left 
#root.left = invertTree(root.right)
#root.right = invertTree(tmp)
#root
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
