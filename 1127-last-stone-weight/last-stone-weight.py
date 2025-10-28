class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)<=1:
            return 0 if len(stones)==0 else stones[0]
        self.maxHeap=[-n for n in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap)>=2:
            wt1=heapq.heappop(self.maxHeap)
            wt2=heapq.heappop(self.maxHeap)
            heapq.heappush(self.maxHeap,wt1-wt2)
        return abs(self.maxHeap[0])
        