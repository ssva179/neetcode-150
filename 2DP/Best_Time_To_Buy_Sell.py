#everyday if we have a slot we can buy if we have already brought something we have to pick best time to sell
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}
        def tp(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in mem:
                return mem[(i,buy)]
            skip = tp(i+1, buy)
            if buy:
                b = tp(i+1, not buy) - prices[i]

                mem[(i,buy)] = max(b,skip)
            else:
                sell = tp(i+2,not buy) + prices[i] 
                mem[(i,buy)] = max(sell, skip)
                print(mem[(i, buy)])
            return mem[(i, buy)]
        return tp(0, True)
