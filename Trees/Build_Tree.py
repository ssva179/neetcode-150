# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder will always have root first -> whe  rebuilding it will always be checked first
#use inorder to know where to split tree
#example:  preorder = [1,2,3,4], inorder = [2,1,3,4]
# [1] -> root 
#inorder = [2],1,[3,4] -> inoder will tell you where to split 
#             / \
#            2  3,4
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        splitVal = inorder.index(preorder[0])


        root.left =self.buildTree(preorder[1:splitVal+1], inorder[:splitVal])
        root.right =self.buildTree(preorder[splitVal+1:], inorder[splitVal+1:])
        return root
