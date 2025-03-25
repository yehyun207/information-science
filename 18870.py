import sys

input = sys.stdin.readline # 입력을 받는다.

n = int(input()) # 몇 번
arr = list(map(int, input().split()))

arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')