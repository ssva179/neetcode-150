#Clarify → Return first and last index of target appearance they are in order so just have to find start and end
#Edge Case: What if not there? -> has to be handled differently that target = 1 -> [1] becuase that does return 0,0 but target = 5 in [1] must return [-1, -1]

#Example: nums = [5,7,7,8,8,10], target = 8 the first appearance is at index 3 then the last at 4 so we return [3, 4]


#Brute force → iterate through entire array and first find start then end of appearances
#Optimize → binary seach we can use it to eliminate parts of array we dont need to look at aka too big or too small
#Complexity: brute O(n) -> optimized: O(log n)
#Pseudocode → 
    #initialize left and right to start and end
    #first find first occurance then last occurance
    #while l <= r:
        #we find middle
        #if value != target we shift based on < > 
        #if value = target:
            #we first respective first or last occurance
    #return least weight
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = 0 
        last = 0
        left = 0
        right = len(nums)-1
        found = False

        #first occurance:
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                found = True
                first = mid
                #we decrease to find first occurance bc if there is ealier occurance it will show up before curr index in array
                right = mid - 1
        #last occurance:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                found = True
                last = mid
                left = mid + 1
        if found:
            return [first, last]
        else:
            return [-1,-1]
