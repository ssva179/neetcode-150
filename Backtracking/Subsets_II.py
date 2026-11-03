#similar to sum where we just sort before we find the subsets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        currSet = []
        def dfs(i):
            if i >= len(nums):
                res.append(currSet.copy())
                return
            #case where we include it
            currSet.append(nums[i])
            dfs(i+1)
            #case were we skip and update i until cand[i] != curr
            curr = nums[i]
            while i+1 < len(nums) and curr == nums[i+1]:
                i +=1
            currSet.pop()
            dfs(i+1)
        dfs(0)
        return res
        
