import sys
answer = {}
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x in answer:
        answer[x] +=1
    else:
        answer[x] = 0


print(sorted(answer.items(),key= lambda x: (-x[1],x[0]) )[0][0])