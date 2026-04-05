class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ%2: return False
        target = summ//2

        dp = [[False]*(target+1) for _ in range(len(nums)+1)]

        for arr in dp: arr[0] = True

        for i in range(len(dp)-1):
            num = nums[i]
            for j in range(len(dp[0])):
                if j-num<0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
            if dp[i][-1]: return True

        return False



        