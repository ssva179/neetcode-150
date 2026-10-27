# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#currNode diameter = maxleft height + max right height
#pseudocode
#helper height 
#if not root:
    #return 0
#lef = height(root.left)
#right = height(root.right)
#d = left + right
#rest = max(diameter(root.left), diameter(root.right)
#return max(d, rest)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)

        diameter = left + right
        rest = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diameter, rest)


        

    def calcHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.calcHeight(root.left), self.calcHeight(root.right))
