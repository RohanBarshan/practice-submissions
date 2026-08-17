class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for n in nums:
            heapq.heappush(res, n)

            while len(res) > k:
                heapq.heappop(res)
        return res[0]