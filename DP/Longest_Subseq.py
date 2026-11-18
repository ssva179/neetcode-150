#OPT(i) -> longest increasing sequence to i
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [0] * len(nums)

        for i in range(len(nums)):
            mem[i] =1
            for j in range(i):
                if nums[i] > nums[j]:
                    mem[i] =max(mem[i], 1 + mem[j])
        
        return max(mem)
