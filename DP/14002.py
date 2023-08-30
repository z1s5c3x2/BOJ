import sys
input = sys.stdin.readline
n = int(input())
ilist = list(map(int,input().split()))
dp=list()
dp=[1]
for x in range(1,n):
    tmp = [1]
    for y in range(x):
        if ilist[x] > ilist[y]:
            tmp.append(dp[y]+1)
    
    dp.append(max(tmp))
mx = max(dp)
cnt = mx
ans = []
for x in range(n-1,-1,-1):
    if dp[x] == cnt:
        ans.append(ilist[x])
        cnt -=1
print(mx)
print(*ans[::-1])