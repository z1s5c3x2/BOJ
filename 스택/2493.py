n = int(input())
list1 = list(map(int,input().split()))
stk = []
answer= []

for x,v in enumerate(list1):
    while stk:
        if list1[stk[-1][0]]< list1[x]:
            stk.pop()
        else:
            answer.append(stk[-1][0]+1)
            break
    if not stk:
        answer.append(0)
    stk.append([x,v])

print(*answer)