# 787. Cheapest Flights Within K Stops
import heapq  # heap queue, aka priority queue
from collections import defaultdict
# https://docs.python.org/3/library/heapq.html
# https://docs.python.org/3/library/collections.html

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        if not flights or not flights[0]:
            return -1

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, src, 0)] # price, startNode, visitedCount(how many flights): K
        while heap:
            tempPrice, tempSrc, visitedCount = heapq.heappop(heap)

            if tempSrc == dst:  # found the cheapest price from src to dst
                return tempPrice
            if visitedCount > K: # if visitedCount exceeds K (visitedCount - 1 = stops)
                continue

            for nextDst, nextPrice in graph[tempSrc]:
                heapq.heappush(heap, (tempPrice + nextPrice, nextDst, visitedCount + 1))

        return -1  # could not find the cheapest price from src to dst
