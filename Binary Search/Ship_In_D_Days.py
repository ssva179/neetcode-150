#Clarify → We have a list with packages each og weight[i]. Every day we can place packages on the truck but we must make all deliveries within a specified number of days.
#What is the capacity of the ship??
#Edge Case: one day means we have to ship everything in one day

#Example: weights = [1,5,4,4,2,3], days = 3 We can try 5 day 1: 1 day 2: 5 day 3: 4 and then we cant so we know we have to go up. 8 day 1: 1,5 day 2: 4, 4 day 3: 2, 3 and it works 

#Brute force → Try all combinations ranging from 1 to max and see which is the least amount of weight we can deliver all packaged in 
#Optimize → binary seach we can still use a range but we can begin in the middle and each iteration decrease our range by half
#Complexity: O(n log n)
#Pseudocode → 
    #get our range min= max(weight) in array bc we cant load 1/2 of a      package max = all weights in one day (Sum)

    #while min <= max:
        #we find middle
        #if mid value workd we shift right trying smaller cap
        #if it doesnt work we shift left to try a bigger capacity
    #return least weight
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        leftMin = max(weights)
        rightMax = sum(weights) 
        
        while leftMin <= rightMax:
            mid =(rightMax+leftMin)//2
            currdays = 1
            totalWeight = 0
            for w in weights:
                if totalWeight + w > mid:
                    totalWeight = 0
                    currdays +=1
                totalWeight += w
            if currdays <= days:
                rightMax = mid - 1
            elif currdays > days:
                leftMin = mid + 1
        return leftMin
