#Clarify → Keep track of max lenght of substring before a character repeats
#Examples & edge cases → empty string 
#Brute force → look through the array and and from every index look at the longest substring we can make. 
#Optimize → window approach shift right when duplicate is detected and keep #track of longest sequence
#Pseudocode → 
    #iterate through the string
        #if we have not seen char add to set
        #if we have seen
            #shift left pointer and remove that char from set
            #is this current substring longer than previous max
    #return max length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res, r-l+1)
        return res
