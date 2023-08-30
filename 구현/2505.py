import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
list2 = list(list1)

check1 = []
check2 = []
for x in range(1,n+1):
    idx = list1[x-1]
    if len(check1) > 2:
        break
    if x != idx:
        idx = list1.index(x)
        start,end = x-1,idx+1
        list1[start:end] = reversed(list1[start:end])
        check1.append([x,idx+1])
for x in range(n,0,-1):

    idx = list2[x-1]
    if len(check2)  > 2:
        break
    if x != idx:
        idx = list2.index(x)
        start,end = idx,x
        list2[start:end] = reversed(list2[start:end])
        check2.append([idx+1,x])

if len(check2) == 2  or len(check1) == 2:
    if len(check2) == 2:
        for x in check2:
            print(*x)
    elif len(check1) == 2:
        for x in check1:
            print(*x)

elif len(check2) == 1  or len(check1) == 1:
    print(1,1)
    if len(check2) == 1:
        for x in check2:
            print(*x)
    elif len(check1) == 1:
        for x in check1:
            print(*x)
else:
    print(1,1)
    print(1,1)