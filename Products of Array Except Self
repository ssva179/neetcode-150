#Clarify: Append products of all elements of the list except current index
#Examples & edge cases: [-1,0,1,2,3] would return all 0 except for index 1 because any product including 0 would be zero
#edge case: if there is a 0 in list my division method would fail
#Brute force: nested loop where we just multiply all numbers except number at current index 
#Optimize: we could run through the list twice once to find the product of all numbets, then iterate again dividing by current index O(2n) = O(n)
#Pseudocode:
#looked at video for explanation but tried to code it for myself

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        i = len(nums)-1
        while i > -1:
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
            i = i-1
        return output
