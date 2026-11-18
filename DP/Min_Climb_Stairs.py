#Min cost to reack top of staircase
#OPT(i) -> min total cose to reach step i
#options -> min(cost[i-1]+OPT(i-1),cost[i-2]+ OPT(i-2))
#Base cases ->  start at the index 0 or the index 1 floor there is nothing before this the cost to get to here is both 0
#           |     OPT(i-1) + cost[i-1]
# OPT(i) =  |min(                      )
#           |     OPT(i-2) + cost[i-2]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        opt = [0] * (len(cost)+1)
        opt[0] = 0
        opt[1] = 0
        for i in range(len(opt)):
            if i == 0 or i ==1:
                continue
            oneth = opt[i-1] + cost[i-1]
            twoth = opt[i-2] + cost[i-2]
            opt[i] = min(oneth, twoth)
        return opt[len(cost)]
