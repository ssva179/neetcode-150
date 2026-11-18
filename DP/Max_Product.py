#OPT(i)-> max product of a continuous sum ending at i
#we can either continue the subarray or we can say the current max is greater than including the next number
#opt(i) = max(i, opt(i-1)*nums[i])
#base opt[0] -> nums[0]
#negative case? -> keep track of min and max bc a negative min might == a very large max if multiplied with a negative number
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        lmin, lmax = 1, 1 #-> has to be 1, 0 would cause 0 product
        for i in range(len(nums)):
            prevMin = lmin
            lmin = min(nums[i], lmin*nums[i],lmax*nums[i])
            lmax = max(nums[i], prevMin*nums[i], lmax*nums[i])
            currMax = max(currMax, lmax)
        return currMax
