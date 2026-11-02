#pseudocode 
#stones -> heapify(max heap)
#pop 2 largest elements
    #while len(heap) > 1:
        #if x == y:
            #insert nothing back to heap 
        #if x < y:
            #insert y - x into heap 
#return heap.pop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            if x < y: #bc they are negative so the smallets
                diff = -(-(x) - -(y))
                heapq.heappush(stones, diff)
        if stones:
            return -(heapq.heappop(stones))
        else: 
            return 0
