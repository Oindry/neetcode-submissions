import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a frequency dictionary using Counter
        freq_map = Counter(nums)
        heap=[]
        for num,freq in freq_map.items():
            heapq.heappush(heap, (freq,num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq,num in heap]
                