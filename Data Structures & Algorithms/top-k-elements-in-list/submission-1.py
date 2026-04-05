class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = defaultdict(int)

        for num in nums:
            mapp[num]+=1
        q = []
        for key in mapp:
            if len(q)<k:
                heapq.heappush(q,(mapp[key], key))
            else:
                if mapp[key]>q[0][0]:
                    heapq.heappop(q)
                    heapq.heappush(q,(mapp[key], key))

        ans = []
        for i in range(k):
            _, value = heapq.heappop(q)
            ans.append(value)


        return ans

        