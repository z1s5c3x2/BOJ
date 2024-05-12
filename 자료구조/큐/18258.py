from collections import deque as q
import sys
input = sys.stdin.readline
dq = q()
answer = []
for _ in range(int(input())):
    tmp = input().split()
    try:
        if tmp[0]=="push":
            dq.append(tmp[1])
        elif tmp[0]=="pop":
            answer.append(dq.popleft())
        elif tmp[0]=="size":
            answer.append(len(dq))
        elif tmp[0]=="empty":
            answer.append(1 if len(dq)==0 else 0 )
        elif tmp[0]=="front":
            answer.append(dq[0])
        else:
            answer.append(dq[-1])
            
    except:
        answer.append(-1)

print(*answer,sep='\n')