#min heap of size k only pop in elements that are larger
#arrange in min heap only add if element is larger than "leaf" nodes
#put all nodes in a min heap and pop until the heap is of size k

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k 
        heapq.heapify(self.minheap)
        
        while len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        
#add value to heap (heapify), then pop lowest
#check if the heap has <= k elements
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
