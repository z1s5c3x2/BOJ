import sys
input = sys.stdin.readline

n = int(input())
numlist = sorted(list(map(int,input().split())))
ans = 1
for x in numlist:
    if ans < x:
        break
    ans+=x

print(ans)