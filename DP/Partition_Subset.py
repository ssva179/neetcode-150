#at each num we either include it or we dont whichever results in a success we return is it reaches a point greater than remaining we dont use it
#case diff == 0, diff < 0, we reach the end of nums
#to split into two we need the sum of all umber in the list//2 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        goal = sum(nums)//2
        memo = {}
        def tp(i, rest):
            if rest == 0:#we reach goal
                return True
            if rest < 0:
                return False
            if i == len(nums):
                return False
            if (i, rest) in memo:
                return memo[(i, rest)]
            #we can try the next number or not
            return tp(i+1, rest-nums[i]) or tp(i+1, rest)
        return tp(0, goal)
