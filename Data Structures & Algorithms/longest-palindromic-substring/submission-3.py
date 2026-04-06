class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * (len(s)+1) for _ in range(len(s)+1)]

        ans = 1
        a_s = s[0]
        for i in range(len(s)):
            dp[i][i] = 1
            if i>=1:
                if s[i-1] == s[i]: 
                    dp[i-1][i] = 2
                    ans = 2
                    a_s = s[i-1:i+1]
        
        for i in range(2, len(s)):
            for j in range(len(s)-i):
                x = j
                y = j+i

                if s[x] == s[y] and dp[x+1][y-1] !=0 :
                    dp[x][y] = dp[x+1][y-1] + 2
                    
                    if dp[x][y] > ans:
                        ans = max(ans, dp[x][y])
                        a_s = s[x:y+1]
        # print(ans)
        # for d in dp:
        #     print(d)
        return a_s
                




            

        