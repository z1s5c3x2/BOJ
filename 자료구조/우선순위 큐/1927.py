import heapq
import sys
input = sys.stdin.readline
hq = []
answer = []
for _ in range(int(input())):
    n = int(input())
    if  n == 0:
        if len(hq) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(hq))    
    else:
        heapq.heappush(hq,n)
    

print(*answer,sep='\n')


