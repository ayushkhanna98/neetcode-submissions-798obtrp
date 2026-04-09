class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapp = {}


        sett = set(nums)
        maxx = 0

        for num in nums:
            if num not in sett: continue
            count = 1
            t = num + 1
            sett.remove(num)
            while t in sett:
                count+=1
                sett.remove(t)
                t = t+1
            if t in mapp:
                count+=mapp[t]
            

            mapp[num] = count
            maxx = max(maxx, count)
        

        return maxx





        