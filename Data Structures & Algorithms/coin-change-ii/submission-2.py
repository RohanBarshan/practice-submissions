class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)-1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                #count the ways to get the amount if we skip the current coin
                nextDP[a] = dp[a]
                # check if we can use the current coin
                if a - coins[i] >= 0:
                    # add the ways of using the current coin
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
