class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)

        for num in nums:
            mapp[num]+=1
        q = []
        for key in mapp:
            heapq.heappush(q,(-mapp[key], key))
        ans = []
        for i in range(k):
            _, value = heapq.heappop(q)
            ans.append(value)


        return ans

        