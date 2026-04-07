class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        ans = self.recurse(word1, word2, 0,0, cache)
        print(cache)
        return ans

    def recurse(self, w1, w2, i, j, cache) -> int:

        #base cases
        
        if j>=len(w2):
            return  len(w1) - i
        
        if i>=len(w1):
            return  len(w2) - j 
        
        if (i,j) in cache: 
            return cache[(i,j)]
        delete = sys.maxsize
        update = sys.maxsize
        replace = sys.maxsize
        ans = sys.maxsize
        if w1[i] == w2[j]:
            #no update
            noUpdate = self.recurse(w1,w2,i+1,j+1, cache)
            ans = min(ans,noUpdate)

        
        #delete 
        delete = self.recurse(w1,w2,i+1,j, cache) + 1

        #update 
        update = self.recurse(w1,w2,i,j+1, cache) + 1

        #replace
        replace = self.recurse(w1,w2,i+1,j+1, cache) + 1

        ans = min(delete, update, replace, ans)

        # if ans-count<0: print(ans,count, ans - count)
        cache[(i,j)] = ans
        return ans








        