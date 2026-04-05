class Solution:
    def countSubstrings(self, s: str) -> int:

        dp = [[0] * (len(s) + 1) for _ in range(len(s)+1)]

        count = 0
        for i in range(len(s)):
            dp[i][i] = 1
            count+=1
            if i>=1 and s[i-1] == s[i]:
                dp[i-1][i] = 1
                count+=1

        
        for i in range(2,len(s)):
            for j in range(0,len(s)-i):
                x = j
                y = i+j
                if s[x] == s[y] and dp[x+1][y-1] == 1:
                    dp[x][y] = 1
                    count+=1


        return count

        