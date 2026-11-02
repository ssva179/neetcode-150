# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#pseudocode:
#if not node:
    #return 0
#dfs()
    #if good node:
        #res+=1
    #max = max(node.val, currmax)
    #check the rest of the tree
#return dfs(node)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 0
            if node.val >= maxVal:
                maxVal = max(maxVal, node.val)
                return 1 + dfs(node.left, maxVal) + dfs(node.right, maxVal)
            else:
                return dfs(node.left, maxVal) + dfs(node.right, maxVal)
        return dfs(root, root.val)
