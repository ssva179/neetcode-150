
class Solution:
    def countSubstrings(self, s: str) -> int:
        mem = [[False] * len(s) for _ in range(len(s))]
        total = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or mem[i + 1][j - 1]):
                    mem[i][j] = True
                    total += 1

        return total
