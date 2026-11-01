# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#pseudocode
#BFS -> but instead of looking at it from ledt to right we look at it from right to left. Then at each "level" we add only the "front" of the queue to the results list.
#Example
#               1
#              / \
#             2   3
#            / 
#           4
#          /
#         5  
#queue(add root) -> 1 ->this would be the first level we add 1 to the results [1]
# now add the children but from right to left -> 2 3 ->
#now we add "first" to results [1,3]
#add children 4 -> [1, 3, 4]
#add children 5 -> [1,3,4,5]
#return list


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = []
        queue.append(root)
        results = []
        while queue:
            results.append(queue[-1].val)
            parents = len(queue)
            for i in range(parents):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return results
