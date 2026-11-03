#you have #letterspernumber * everynumber of possible combinations
#add every possible character to the current string until you have one char from every number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            #we get every char from a number
            for c in digitToChar[digits[i]]:
                dfs(i+1, curr + c)
                curr[:-1]
        if digits:
            dfs(0, "")
        return res


        
