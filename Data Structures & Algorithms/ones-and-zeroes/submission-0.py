class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m ,n):
            if i == len(strs):
                return 0
            
            if (i,m,n) in dp:
                return dp[(i,m,n)]
            
            mCnt, nCnt = strs[i].count("0"), strs[i].count("1")
            
            # Option 1: Skip the current string
            res = dfs(i + 1, m, n)
            
            # Option 2: Include the current string (if possible)
            if mCnt <= m and nCnt <= n:
                res = max(res, 1 + dfs(i + 1, m - mCnt, n - nCnt))
            
            dp[(i, m, n)] = res
            return res
        return dfs(0,m,n)