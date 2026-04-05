class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        mapp = defaultdict(list)

        for time in times:
            a = time[0]
            b = time[1]
            t = time[2]

            mapp[a].append((b,t))


        visited = set()
        q = []
        maxTimeTaken = 0
        heapq.heappush(q,(0,k))

        while q:

            time, node = heapq.heappop(q)

            if node in visited: continue

            maxTimeTaken = max(maxTimeTaken, time)
            visited.add(node)

            for neighbour in mapp[node]:
                nei = neighbour[0]
                t = neighbour[1]
                heapq.heappush(q, (time+t,nei))
        

        if len(visited) == n:
            return maxTimeTaken
        else:
            return -1



    

        