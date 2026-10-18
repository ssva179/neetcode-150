#pseudocode
#get max of piles
#perform binary search on that range
#if we find a k value that allows us to eat in <= h hours we keep that
#if we find a k value that is < curr k we update
#we return min k value found
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        values = max(piles)
        l = 1
        r = values
        currK = r
        while l <= r:
            m = (r+l)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours <= h:
                currK = min(currK, m)
                r = m - 1
            elif hours > h:
                l = m + 1
        return currK
