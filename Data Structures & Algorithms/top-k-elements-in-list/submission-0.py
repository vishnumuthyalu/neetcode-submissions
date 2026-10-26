
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        frequencies = Counter(nums)

        for number, count in frequencies.items():
            heapq.heappush(heap, (count, number))

            if len(heap) > k:
                heapq.heappop(heap)
        elements = [element for count, element in heap]
        return elements
