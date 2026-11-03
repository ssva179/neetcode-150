#Sort input array to prevent duplicates
#for first side update as normal for right side keep updating i until next val is not == to curr val
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        currSet = []
        def dfs(i):
            if sum(currSet) == target:
                res.append(currSet.copy())
                return
            if i >= len(candidates) or sum(currSet) > target:
                return
            #case where we include it
            currSet.append(candidates[i])
            dfs(i+1)
            #case were we skip and update i until cand[i] != curr
            curr = candidates[i]
            while i+1 < len(candidates) and curr == candidates[i+1]:
                i +=1
            currSet.pop()
            dfs(i+1)
        dfs(0)
        return res






