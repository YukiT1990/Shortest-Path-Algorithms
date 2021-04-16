# 743. Network Delay Time
import heapq  # heap queue, aka priority queue
from collections import defaultdict
# https://docs.python.org/3/library/heapq.html
# https://docs.python.org/3/library/collections.html

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:



        travelTime = [0] + [float('inf') for _ in range(n)]  # initial values are infinite
        graph = defaultdict(list)
        heap = [(0, k)]


        for u, v, w in times:
            graph[u].append((v, w))
        while heap:
            time, node = heapq.heappop(heap)  # heapq.heappop(heap)
            if time < travelTime[node]:
                travelTime[node] = time
                for v, w in graph[node]:
                    heapq.heappush(heap, (time + w, v))  # heapq.heappush(heap, item)

        maxTime = max(travelTime)

        if maxTime < float('inf'):
            return maxTime
        else:  # there are any nodes which are not visited
            return -1
