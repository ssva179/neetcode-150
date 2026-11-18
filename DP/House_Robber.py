#Clarify: How much money can we rob
#OPT(i) -> max amount of money we can rob with i houses
#at house i we can either rob the house or skip it 
#Options -> max (opt[i-2] + i or opt(i-1))
#base cases -> house(0) = nums[0] house[1] = max(nums[0],nums[1])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        money = [0]*len(nums)
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(len(nums)):
            if i == 0 or i == 1:
                continue
            money[i] = max(money[i-2]+nums[i], money[i-1])
        return money[len(nums)-1]
        
