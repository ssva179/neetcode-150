#min # of coins that = amount
# if avalibale coins cannot meet exact amount return -1
#Clarify are coins sorted
#OPT(i) -> number of coins needed to meet amount i
#opt(i) = 1 + opt(i-currcoin)
#memoizartion = [-1]*amount+1 ->basecase
#base cases -> amt = 0 -> return 0 if i < 0 -> -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amt = [-1]*(amount+1)
        amt[0] = 0
        def tp(i):#curr amount
            if i == 0:
                return 0
            if amt[i] != -1:#we have found a "min"
                return amt[i]
            curr = 10001
            for c in coins:
                left = i - c
                if left >= 0:
                    curr = min(curr, 1+tp(left))
            amt[i]=curr
            return curr
        if tp(amount) >= 10001:
            return -1
        else:     
            return tp(amount)
