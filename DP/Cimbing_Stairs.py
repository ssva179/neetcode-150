#Options at this step climb either 1 or 2 steps
#at i you came from i - 1 or i - 2 because You can climb with either 1 or 2 steps at a time.
#Base Cases Step 0 -> 1 step 1 -> 1 theres only one way to reach both of these steps
#OPT(i) -> total distict ways we can reach step n taking either 1 or 2 steps
# -> = OPT(i-1) + OPT(i-2)
#Edge cases: what if there are 0 Steps-> constraints 1 <= n <= 45
#O(n) -> we look a n steps 
class Solution:
    def climbStairs(self, n: int) -> int:
        opt = [0]*(n+1)
        #base cases
        opt[0] = 1
        opt[1] = 1
        for i in range(len(opt)):
            if i == 0 or i == 1:
                continue
            opt[i] = opt[i-1] + opt[i-2]
        return opt[n]
