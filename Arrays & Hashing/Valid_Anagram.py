# 8 steps
#Clarify: two words have to have every letter have and equal count
#how can I keep count?
#Examples: "racecar" & "carrace" -> r = count 2 for both strings c = 2 for both and a =2 for both so we return true
#Edge cases: empty string? uneven strings?
#brute force: arrange both strings in alphabetical order
#Optimize: find a way to keep track of the count of each letter  for both words O(n+m)
#Pseudocode: 
    #edge case check for equal length
    #iterate through one of the strings
        #keep track of repeated letters and add to their count for
        #both strings
    #iterate through counts and check to see they are equal for each letter
    #if you find a mismatch return false else true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False;
        #It wasn't clicking to have two dicts so i looked at solution
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = 1+ count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for key in count_s:
            if count_s[key] != count_t.get(key, 0):
                return False;
        return True;
