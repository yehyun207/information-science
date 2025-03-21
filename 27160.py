import sys
input = sys.stdin.readline

n = int(input())

d = {}

for _ in range(n):
    S,N = map(str, input().split())
    try:
        d[S] += int(N)
    except:
        d[S] = int(N)

check = False
for i in d.values():
    if i == 5:
        check = True

if check:
    print("YES")
else:
    print("NO")