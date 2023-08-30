import sys
import heapq
input = sys.stdin.readline
n,k = map(int,input().split())
jlist = []
for _ in range(n):
    heapq.heappush(jlist,list(map(int,input().split())))
baglist = sorted([int(input()) for _ in range(k)])
hq=[]
ans = []
res = 0
for x in baglist:
    while jlist and jlist[0][0] <= x:
        heapq.heappush(ans,-jlist[0][1])
        heapq.heappop(jlist)
    if ans:
        res += -heapq.heappop(ans)
    elif not jlist:
        break
print(res)