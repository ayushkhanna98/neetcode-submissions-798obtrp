from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        min_heap = [(0, k)]
        
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            
            # Ignore stale heap entries
            if curr_dist > dist[node]:
                continue
            
            for nei, weight in graph[node]:
                new_dist = curr_dist + weight
                
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(min_heap, (new_dist, nei))
        
        ans = max(dist.values())
        return ans if ans != float('inf') else -1