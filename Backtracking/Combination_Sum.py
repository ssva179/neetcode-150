#example nums = [2,5,6,9]
#target = 9
#nums[0] = 2 9-2 = 7 7-2 - 5
#brtue force decision tree down each number/ doesnt prevent permutations
#Optimize: down decision tree skip num on one side
#pseudocode:
#start at index 0 at each recursive step add num at index 0 to one side and not to the other side
#if lists sum = target add to soln
#if it > target move on to other nums in list
#return res
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        currSum = []
        def dfs(i):
            if sum(currSum) == target:
                res.append(currSum.copy())
                return
            if i >= len(nums) or sum(currSum) > target:
                return
            currSum.append(nums[i])
            dfs(i)
            currSum.pop()
            dfs(i+1)
        dfs(0)
        return res

        
