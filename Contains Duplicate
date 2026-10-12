# 8 steps
#Clarify: We want to check every unique value in a list 
#         if we find a value that is not unique we      #         return true Do we account for empty lists?
#Examples: [1, 2, 3, 3] we check 1 and compare to every element and then we do it for two once we get to 3 we find element at index 3 is also 3 so we return true
#Edge cases: empty lists? 
#brute force: nested loop where we look at every item in the list and loop through list again to compare it to every remaining element
#Optimize: find a way to keep track of numbers we have already seen and just recall that list as we go O(n)
#Pseudocode: 
    #iterate through array
        #have we seen this number?
            #if yes -> return true
    #We never saw a dupe -> return false 



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = {}
        for i in range(len(nums)):
            if nums[i] in dupe:
                return True;
            else:
                dupe[nums[i]]=0;
        return False;
