class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum,0)
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum