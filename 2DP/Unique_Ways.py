#OPT[m][n]-> we have to add up all possible paths
#Base Cases -> we reach a cell thats out of range we return 0 we reach the bottom right corner we return 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1]*n for _ in range(m)]
        #i = m , j = n
        def tp(i,j):
            #base cases
            if (i, j) == (m-1, n-1):
                return 1
            if i > m-1 or j > n-1:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            print(i,j)
            memo[i][j] = tp(i+1,j) + tp(i, j+1)
            return memo[i][j]
        
        return tp(0,0)
