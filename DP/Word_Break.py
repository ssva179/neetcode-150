#OPT(i) -> up to index i can we say that this should return true
#cases -> mem[i] already found of if we have reached end of the string, or we cannot find a matching word
#we keep track of indexes wehre we find true or false
#At i we iterate through the words in wordDict if one matched we move on to try the next one 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [None] * len(s)

        def tp(i):
            #case 1 we have completed the string 
            if i == len(s):
                return True
            if mem[i] != None:
                return mem[i]
            res = None
            for w in wordDict:
                if s[i: i + len(w)] == w:
                    res = tp(i + len(w))
                if res:
                    mem[i] = True
                    return True
            mem[i] = False
            return False
            
        return tp(0)
