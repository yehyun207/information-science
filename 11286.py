import heapq ## 힙 큐를 사용하기 위해 임포트
import sys

min_heap = [] ## min_heap 배열 생성
n = int(sys.stdin.readline()) ## 몇 번 반복할건지 n값 받아오고

for i in range(n): ## n번 반복
    x = int(input())

    if x == 0: ## x가 0이랑 같다면
        if min_heap: ## 배열에 비어있지 않다면
            print(heapq.heappop(min_heap)[1]) ##최소 힙에서 가장 작은 절대값의 원래 값을 제거하고 출력한다
        
        else:
            print(0)
            
    else: ## 0이 아니라면 
            heapq.heappush(min_heap, ((abs(x), x)))## 절대값으로 배열에 값을 추가한다.