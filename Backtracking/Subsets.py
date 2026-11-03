#Following the decision tree at every level we 
#just chode to add the next num to subset and not 
#adding it. As you go down the list this created distinct subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr =[]
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            #include
            curr.append(nums[i])
            dfs(i+1)
            #dont include
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res

        
