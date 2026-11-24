import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kList = [(-self.euclidean_dist(p), p) for p in points[:k]]

        heapq.heapify(kList)
        res = []

        for i in range(k, len(points)):
            dist = self.euclidean_dist(points[i])
            smallest = kList[0]
            if -dist > smallest[0]:
                heapq.heappop(kList)
                heapq.heappush(kList, (-dist, points[i]))

        for i in range(k):
            res.append(heapq.heappop(kList)[1])

        return res

    def euclidean_dist(self, point):
        return math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2)
