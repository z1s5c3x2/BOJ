import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
lis1 = [1]*n
lis2 = [1]*n

for x in range(1,n):
    for y in range(x):
        if list1[x] > list1[y]:
            lis1[x] = max(lis1[x],lis1[y]+1)
list1 = list1[::-1]

for x in range(1,n):
    for y in range(x):
        if list1[x] > list1[y]:
            lis2[x] = max(lis2[x],lis2[y]+1)
lis2 = lis2[::-1]
if n==1:
    print(1)
    exit()
ans = 0

for x in range(len(lis1)):
    for y in range(x,len(lis2)):
        ans = max(ans,lis1[x]+lis2[y]-1)
    
print(ans)
