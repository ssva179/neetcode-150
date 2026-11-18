#same as house robber one except we either rob house 1 or we dont and take the max of including either first house of last house
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        rob1 = self.robH(nums[1:])
        roblast = self.robH(nums[:-1])
        return max(rob1, roblast)
    

    def robH(self, nums) -> int:
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
