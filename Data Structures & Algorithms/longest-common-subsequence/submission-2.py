class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dp = [[0]*(len(t1)+1) for _ in range(len(t2)+1)]


        for i in range(len(t2)):
            for j in range(len(t1)):
                if t2[i] == t1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-2][-2]

        