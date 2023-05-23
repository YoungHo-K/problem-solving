import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        self._initialize_nums()
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        
    def _initialize_nums(self):
        heapq.heapify(self.nums)        
        
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)