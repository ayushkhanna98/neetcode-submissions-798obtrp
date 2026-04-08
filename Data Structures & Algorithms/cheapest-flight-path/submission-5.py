class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h = []
        mapp = defaultdict(list)

        for o, d, c in flights:
            mapp[o].append((d, c))

        heapq.heappush(h, (0, src, 0))  # cost, city, flights_used
        best = {}

        while h:
            cost, curr, flights_used = heapq.heappop(h)

            if curr == dst:
                return cost

            if flights_used > k:
                continue

            if (curr, flights_used) in best and best[(curr, flights_used)] < cost:
                continue

            best[(curr, flights_used)] = cost

            for nextStop, nextCost in mapp[curr]:
                new_cost = cost + nextCost
                heapq.heappush(h, (new_cost, nextStop, flights_used + 1))

        return -1