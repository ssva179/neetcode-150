#Clarify: the string has to read the same forward and reverse
#Examples & edge cases → "Was it a car or a cat I saw?" you skip over non alphanumeric numbers and then the does read the same forward and backwards
#Brute force → reverse the string then compare to original string
#Optimize → have two pointers one at start one at the end and move inwards checking as you go O(n)
#Pseudocode → 
        #iterate through string start and end
            #are start and end alphanumeric
                #if they are not equal
                    #return False
        #return true#
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start=0
        end= len(s)-1
        s = s.lower()
        while start < end:
            while start < end and not (48 <= ord(s[start]) <= 57 or 97 <= ord(s[start]) <= 122):
                start +=1
            while start < end and not (48 <= ord(s[end]) <= 57 or 97 <= ord(s[end]) <= 122):
                end -=1
            if s[start] != s[end]:
                return False
            start +=1
            end -=1
        return True
