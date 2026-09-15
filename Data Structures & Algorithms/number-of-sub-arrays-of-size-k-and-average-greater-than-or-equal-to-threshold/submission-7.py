class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        windowSum = 0
        count = 0

        for R in range(len(arr)):
            windowSum += arr[R]

            if R - L + 1 == k:

                if windowSum / k >= threshold:
                    count += 1

                windowSum -= arr[L]
                L += 1

        return count