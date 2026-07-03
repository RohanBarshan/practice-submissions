class MedianFinder:

    def __init__(self):
         # Max heap (store negatives because Python only has a min heap)
        self.small = []
        #min heap
        self.large = []

    def addNum(self, num: int) -> None:
        #Decide which heap
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
        else:
            largest_small = - self.small[0]
            if num <= largest_small:
                heapq.heappush(self.small, -num)
            else:
                heapq.heappush(self.large, num)
               # -----------------------------
        # Step 2: Rebalance the heaps
        # -----------------------------

        # Small heap has too many elements
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        elif len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)
        
         # -----------------------------
        # Step 3: Make sure ordering is correct
        # -----------------------------
        if len(self.small) > 0 and len(self.large) > 0:
            largest_small = -self.small[0]
            smallest_large = self.large[0]

            if largest_small > smallest_large:
                small_value = -heapq.heappop(self.small)
                large_value = heapq.heappop(self.large)

                heapq.heappush(self.small, - large_value)
                heapq.heappush(self.large, small_value)
    
        
    def findMedian(self) -> float:

        #small heap has more elements
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Large heap has more elements
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        