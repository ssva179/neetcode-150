#Clarify: find the two indexes whose sum = target. Make sure smaller index
    #is returned first 
#Examples & edge cases:[3,4,5,6] target 7 3+4 = 7 3 = index 0 4 = index 1 
                        #return [0,1] 
        #potential edge case could be empty list? no pair that satisfies
        #problem says we can assume the correct pair exists
#Brute force: nested loop to see if future index plus current index = target
#optimize: store numbers we have seen perform lookup as we go instead of 
            #extra loop O(n)
#pseudocode
        #iterate through nums
            #find = target - curr num
            #have we seen find before?
                #yes? 
                    #return [find index, curr num index]
                #no?
                    #store curr num and index



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            find = target - nums[i];
            if find in seen:
                return [seen.get(find, 0), i];
            else:
                seen[nums[i]] = i;
        return []   
        
