'''
You are given a 2-D array points where points[i] = [xi, yi]
points is a list featuring coordinates of points on an x-y plane
The 2D array is [-100,-100] to [100,100]

you are given the integer k
k and points is small

return the k closest points to the origin

distance between points is calculated using euclidean distance
we only care about distance between points and origin
(sqrt((x1 - x2)**2 + (y1 - y2)**2))
can be written as:
(sqrt((x2)**2 + (y2)**2))
since we dont need the value of distance, we can simplify the equation to:
(x**2 + y**2)

order doesnt matter

input: points = [[0,2],[2,2]], k = 1
points_distance_squared = [4, 8]
minheap = [(4, [0,2]), (8, [2,2])]
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        solution = []
        for i in range(len(points)):
            minheap.append(((points[i][0] ** 2 + points[i][1] ** 2), points[i]))
        heapq.heapify(minheap)
        print(minheap)
        for _ in range(k):
            item = heapq.heappop(minheap)
            solution.append(item[1])
        return solution
        