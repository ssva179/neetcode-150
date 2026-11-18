#if letters match we check diagonally if they dont we check down and right
#Base cases when we reach end of both strings we go back
#
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem= [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i]==text2[j]:
                    mem[i][j] = 1+mem[i+1][j+1]
                else:
                    mem[i][j] = max(mem[i+1][j], mem[i][j+1])
        return mem[0][0]
