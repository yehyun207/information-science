import heapq
import sys

min_heap = []
n = int(sys.stdin.readline())

for i in range(n):
    x = int(input())

    if x == 0:
        if min_heap:
            print(heapq.heappop(min_heap)[1])
        
        else:
            print(0)
            
    else:
            heapq.heappush(min_heap, ((abs(x), x)))