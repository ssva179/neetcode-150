#pseudocode
#pointers from left and right
#while l <= r
    #calculate mid point
    #if mid < target
        #"delete" left side of middle
    #if mid > target:
        #"delete" right values to middle
    #if == to target return index
#else return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == []:
            return -1
        l = 0
        r = len(nums) -1
        while l <= r:
            middle = l + ((r-l)//2)
            if nums[middle] < target: 
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            elif nums[middle] == target:
                return middle
        return -1 
