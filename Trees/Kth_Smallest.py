# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#traverse down the left side of the tree. When we reach the botton we can pop into stack. then pop elements from stack if we reak k=0 we return that value. if not we have to check right side one by one
#Clarification is there always a valid answer or do we account for maybe nodes < k
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            #adding all left nodes
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr=stack.pop()
            k -=1
            #if we get to here were back at root and k > 0
            if k == 0:
                return curr.val
            curr = curr.right
        return curr.val
