class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)

        for s in strs:
            new_s = sorted(s)
            new_s = str(new_s)
            mapp[new_s].append(s)
        
        ans = []
        for k in mapp:
            ans.append(mapp[k])
        

        return ans
        