class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        remainingweight = 0
        maxheap = stones
        heapq.heapify_max(stones)
        while(maxheap):
            print(maxheap)
            if(len(maxheap) == 1):
                remainingweight = heapq.heappop_max(maxheap)
                break
            stoneone = heapq.heappop_max(maxheap)
            stonetwo = heapq.heappop_max(maxheap)
            remaining = stoneone - stonetwo
            if (remaining != 0):
                heapq.heappush_max(maxheap, remaining)
            
        return remainingweight
        

