#Clarify: can two points have the same distance
#find a way to store the distance alogside the pair [d, x, y]
#then sort and return k closest points
#pseudocode
#for every point calculate distance to origin
#heapify
#pop k elements into result for every elem [1:]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            xi= points[i][0]
            yi=points[i][1]
            distance= math.sqrt((0 - xi)**2 + (0 - yi)**2)
            points[i] = [distance, xi, yi]
        heapq.heapify(points)
        for i in range(k):
            point = heapq.heappop(points)
            res.append([point[1], point[2]])

        return res
