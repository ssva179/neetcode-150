
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem ={}

        def tp(i, rem):
            if i == len(nums):
                if rem == 0:
                    return 1
                return 0
            if (i, rem) in mem:
                return mem[(i, rem)]
            #case 1: subtract
            sub = tp(i+1, rem + nums[i])
            #case 2: add curr num
            add = tp(i+1, rem - nums[i])
            mem[(i, rem)] = sub+add
            return mem[(i,rem)]
        return tp(0, target)
