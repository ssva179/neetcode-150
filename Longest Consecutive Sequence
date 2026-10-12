#Clarify: find the longest length of consecutive numbers in array. They do no have to be in order in array
#Examples & edge cases: [0,3,2,5,4,6,1,1] 0,1,2,3,4,5,6 are all consecutive so we would output 7. 
#edge case: empty arrays 
#Brute force: we check every number with all numbers in list to see where we can extend the sequence 
#Optimize: we can store all numbers and then only look for sequences were a number is the smallest of a possible sequence O(n)
#Pseudocode:
    #put all numbers in lookup table
    #iterate through nums
        #does a currNum-1 exist
            #if yes this is not start of consec seq continue
            #if no lets see how long sequence is
                #if this seq longer than curr longest
                    #if yes replace
        # return longest seq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        maxSeq = 0
        for num in nums:
            count[num]=1
        for num in nums:
            seq = 1
            if num-1 in count:
                continue
            else:
                cont = True
                seqNum = num
                while cont:
                    if seqNum+1 in count:
                        seq+=1
                        seqNum+=1
                    else:
                        cont = False
            if seq > maxSeq:
                maxSeq = seq
        return maxSeq
