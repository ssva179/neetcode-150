#OPT(i) -> number of ways to decode the string starting at index i
#We are finding all the ways so we add all possible solutions
#We can either include just i or the next two digits if they are within 1-26 
#Base case-> ifs[i] = o return 0, or we reach end of string
class Solution:
    def numDecodings(self, s: str) -> int:
        mem = [-1] * len(s)

        def tp(i):
            if i == len(s): 
                return 1
            if s[i] == "0":
                return 0
            if mem[i] > -1:
                return mem[i]
            count =0
            #case 1: we use only one digit
            if s[i] != "0":
                count += tp(i+1)
            #case 2: we use both digits
            if i+2 <= len(s) and int(s[i]) > 0 and int(s[i]) < 3:
                if int(s[i]) == 1:
                    count += tp(i+2)
                if int(s[i]) == 2:
                    if int(s[i+1]) < 7 and int(s[i+1]) >= 0:
                        count += tp(i+2)
            mem[i] = count
            return mem[i]
        return tp(0)
