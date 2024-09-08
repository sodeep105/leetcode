class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        maxheap = []
        heapq.heapify(maxheap)
        for key, value in counter.items():
            heapq.heappush(maxheap,[-value,key])
        
        res =[]
        while k > 0:
            value, key = heapq.heappop(maxheap)
            res.append(key)
            k = k-1

        return res        