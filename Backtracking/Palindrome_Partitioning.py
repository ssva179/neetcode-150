class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr =[]

        def dfs(i):
            if i >= len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j+1)
                    curr.pop()
        dfs(0)
        return res
    def isPali(self, s, i, j):
        if s[i:j+1] == s[i:j+1][::-1]:
            return True
        return False



        
