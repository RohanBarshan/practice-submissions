class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L = 0
        curSum = sum(arr[:k - 1])
        total = 0

        for R in range(len(arr) - k + 1):
            curSum += arr[R + k - 1]
            if curSum / k >= threshold:
                total += 1
            curSum -= arr[R]
        return total
