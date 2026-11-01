# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        lists = []
        while queue:
            lists.append([x.val for x in queue])
            parents = len(lists[-1])
            for i in range(parents):
                currP = queue.pop(0)

                if currP.left:
                    queue.append(currP.left)
                if currP.right:
                    queue.append(currP.right)
        return lists
