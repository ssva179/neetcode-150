#curr heap.pop 
#for curr neighbors -> add to heap
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #adj list of weighted graph
        adj = [[] for i in range(n+1)]
        for ui, vi, wi in times:
            #(ui, vi, wi) u -> v 
            #now each index of adj corresponds to all nodes that ui points to
            adj[ui].append((vi, wi))
        visit = set()
        time = 0
        heap = [(0,k)]
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, dist)
            for edge in adj[node]:
                if edge[0] in visit:
                    continue
                distance = dist + edge[1]
                heapq.heappush(heap, (distance, edge[0]))
        if len(visit) == n:
            return time
        
        return -1 




        
