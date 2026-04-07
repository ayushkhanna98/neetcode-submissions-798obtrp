class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        if len(s1) + len(s2) != len(s3): return False
        return self.recurse(s1,s2,s3,0,0, cache)


    

    def recurse(self, s1,s2,s3, i,j, cache) -> bool:

        # base case 

        if i==len(s1) and j == len(s2) and i+j==len(s3):
            return True
        

        if (i,j) in cache:
            return cache[(i,j)]

        case1 = False
        case2 = False 
        k = i+j
        if i<len(s1) and s1[i] == s3[k]:
            case1 = self.recurse(s1,s2,s3,i+1,j, cache)
        if j<len(s2) and s2[j] == s3[k]:
            case1 = self.recurse(s1,s2,s3,i,j+1, cache)
        

        cache[(i,j)] = case1 or case2
        return case1 or case2
        
        